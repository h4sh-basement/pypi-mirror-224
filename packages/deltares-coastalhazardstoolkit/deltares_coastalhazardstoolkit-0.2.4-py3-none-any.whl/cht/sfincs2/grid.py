# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:24:49 2022

@author: ormondt
"""
import time
import os
import numpy as np
from matplotlib import path
from pyproj import CRS, Transformer
import shapely

import xugrid as xu
import xarray as xr
import warnings
np.warnings = warnings

import geopandas as gpd
import pandas as pd

import datashader as ds
import datashader.transfer_functions as tf
from datashader.utils import export_image


class SfincsGrid:
    def __init__(self, model):
        self.model       = model
        self.x0 = None
        self.y0 = None
        self.dx = None
        self.dy = None
        self.rotation = None
        self.nr_cells = 0
        self.nr_refinement_levels = 1
        self.version = 0
        self.data = None
        self.exterior = gpd.GeoDataFrame()

    def build(self,
              x0,
              y0,
              nmax,
              mmax,
              dx,
              dy,
              rotation,
              refinement_polygons=None,
              refinement_levels=None):

        print("Building mesh ...")

        if not refinement_polygons:
            refinement_polygons = []

        start = time.time()

        self.x0 = x0
        self.y0 = y0
        self.dx = dx
        self.dy = dy
        self.nmax = nmax
        self.mmax = mmax
        self.rotation = rotation
        cosrot = np.cos(rotation*np.pi/180)
        sinrot = np.sin(rotation*np.pi/180)
        
        refmax = 0
        if refinement_levels:
            refmax = max(refinement_levels)

        # Loop through refinement gdfs and turn into separate geometries
        ref_pols = []
        for igdf, gdf in enumerate(refinement_polygons):
            ilev = refinement_levels[igdf]
            for p in gdf2list(gdf):
                polygon = {"geometry": p.loc[0].geometry, "refinement_level": ilev}
                ref_pols.append(polygon)
            
        # Number of refinement levels
        nlev = refmax + 1
        self.nr_refinement_levels = nlev
        self.ifirst = np.zeros(nlev, dtype=int)

        # Set refinement mask
        nmx       = []
        mmx       = []
        dxb       = []
        dyb       = []
        refmsk    = []
        inirefmsk = []
        isrefined = []
        
        # Loop through refinement levels to set some constants per level
        for ilev in range(nlev):
            nmx.append(nmax*2**(ilev))
            mmx.append(mmax*2**(ilev))
            dxb.append(dx/2**(ilev))
            dyb.append(dy/2**(ilev))
            refmsk.append(np.zeros((nmx[ilev], mmx[ilev]), dtype=int))
            inirefmsk.append(np.zeros((nmx[ilev], mmx[ilev]), dtype=int))
            isrefined.append(np.zeros((nmx[ilev], mmx[ilev]), dtype=int))
        
        inirefmsk[0] += 1

        # First set initial refinement levels based on polygons
        print("Finding points in polygons ...")
        if ref_pols:
            for ilev in reversed(range(nlev)):
                print("Level " + str(ilev + 1) + " ...")
                # Loop through polygons
                for ipol, polygon in enumerate(ref_pols):
                    # Check if this refinement level ilev matches refinement levels of this polygon
                    if polygon["refinement_level"] == ilev:
                        n0 = 1e9
                        n1 = -1e9
                        m0 = 1e9
                        m1 = -1e9
                        # Rotate polygon to grid in order to get n0, n1, m0 and m1
                        coords = polygon["geometry"].exterior.coords[:]
                        for ipoint, point in enumerate(coords):
                            xp =   cosrot*(point[0] - x0) + sinrot*(point[1] - y0)
                            yp = - sinrot*(point[0] - x0) + cosrot*(point[1] - y0)
                            n0 = min(n0, int(np.floor(yp / dyb[ilev])))
                            n1 = max(n1, int(np.ceil(yp / dyb[ilev])))
                            m0 = min(m0, int(np.floor(xp / dxb[ilev])))
                            m1 = max(m1, int(np.ceil(xp / dxb[ilev])))

                        n0 = max(n0, 0)
                        n1 = max(n1, 0)
                        m0 = max(m0, 0)
                        m1 = max(m1, 0)

                        n0 = min(n0, nmx[ilev] - 1)
                        n1 = min(n1, nmx[ilev] - 1)
                        m0 = min(m0, mmx[ilev] - 1)
                        m1 = min(m1, mmx[ilev] - 1)

                        if m0 == m1 or n0 == n1:
                            continue

                        nmxx = n1 - n0 + 1
                        mmxx = m1 - m0 + 1
                        xcor = np.zeros((4, nmxx, mmxx))
                        ycor = np.zeros((4, nmxx, mmxx))
                        for mm in range(mmxx):
                            m = mm + m0
                            for nn in range(nmxx):
                                n = nn + n0
                                # 4 corner points of this cell
                                xcor[0, nn, mm] = x0 + cosrot*((m    )*dxb[ilev]) - sinrot*((n    )*dyb[ilev])
                                ycor[0, nn, mm] = y0 + sinrot*((m    )*dxb[ilev]) + cosrot*((n    )*dyb[ilev])
                                xcor[1, nn, mm] = x0 + cosrot*((m + 1)*dxb[ilev]) - sinrot*((n    )*dyb[ilev])
                                ycor[1, nn, mm] = y0 + sinrot*((m + 1)*dxb[ilev]) + cosrot*((n    )*dyb[ilev])
                                xcor[2, nn, mm] = x0 + cosrot*((m + 1)*dxb[ilev]) - sinrot*((n + 1)*dyb[ilev])
                                ycor[2, nn, mm] = y0 + sinrot*((m + 1)*dxb[ilev]) + cosrot*((n + 1)*dyb[ilev])
                                xcor[3, nn, mm] = x0 + cosrot*((m    )*dxb[ilev]) - sinrot*((n + 1)*dyb[ilev])
                                ycor[3, nn, mm] = y0 + sinrot*((m    )*dxb[ilev]) + cosrot*((n + 1)*dyb[ilev])
                        for j in range(4):
                            inp0 = inpolygon(np.squeeze(xcor[j,:,:]),
                                             np.squeeze(ycor[j,:,:]),
                                             polygon["geometry"])
                            iok = np.where(inp0)
                            nok = iok[0] + n0
                            mok = iok[1] + m0
                            inirefmsk[ilev][nok, mok] = 1

        # Highest levels have now been set        
        if nlev == 1:
            # Activate all cells
            refmsk[0] = refmsk[0] + 1
        else:    
            # Loop through levels in reverse order to refine cells
            print("Refining cells ...")
            for ilev in reversed(range(nlev)):
                print("Level " + str(ilev + 1) + " ...")
                # Get n0, n1, m0 and m1
                for m in range(mmx[ilev]):
                    for n in range(nmx[ilev]):
                        if not isrefined[ilev][n, m]:
                            # Two reasons to use this block
                            # 1) Neighbor is refined
                            # 2) Initial minimum level is ilev
                            iok = False                          
                            if inirefmsk[ilev][n, m] == 1:
                                # This cell lies within a refinement polygon at this level
                                iok = True
                            else:
                                # Check for neighbors (only for coarser levels)
                                if ilev<nlev - 1:
                                    # Left
                                    if m>0:
                                        if isrefined[ilev][n, m - 1]:
                                            iok = True
                                    # Right
                                    if m<mmx[ilev] - 1:
                                        if isrefined[ilev][n, m + 1]:
                                            iok = True
                                    # Top
                                    if n>0:
                                        if isrefined[ilev][n - 1, m]:
                                            iok = True
                                    # Bottom
                                    if n<nmx[ilev] - 1:
                                        if isrefined[ilev][n + 1, m]:
                                            iok = True

                            if iok:                            
                                # Should use this cell
                                refmsk[ilev][n, m] = 1
                                # Set lower level cells to refined so that we know in lower
                                # refinement levels that they should not be used
                                nn = n
                                mm = m
                                for jlev in reversed(range(ilev)):
                                    if odd(nn):
                                        nnu = int((nn + 1)/2 - 1)
                                    else:
                                        nnu = int((nn)/2)
                                    if odd(mm):
                                        mmu = int((mm + 1)/2 - 1)
                                    else:
                                        mmu = int((mm)/2)
                                    isrefined[jlev][nnu, mmu] = 1
                                    nn = nnu
                                    mm = mmu                        

                                # Also set 3 other blocks also to 1, unless already refined
                                [nnbr,mnbr] = get_neighbors_in_larger_cell(n, m)
                                for j in range(4):
                                    if nnbr[j]>-1 and nnbr[j]<=nmx[ilev] - 1 and mnbr[j]>-1 and mnbr[j]<=mmx[ilev] - 1:
                                        if not isrefined[ilev][nnbr[j], mnbr[j]]:
                                            refmsk[ilev][nnbr[j], mnbr[j]] = 1


        # Count total number of cells
        if nlev == 1:
            nb = mmx[ilev] * nmx[ilev]
            level = np.zeros(nb, dtype=int)
        else:    
            print("Counting number of cells ...")
            nb = 0
            for ilev in range(nlev):
                for m in range(mmx[ilev]):
                    for n in range(nmx[ilev]):
                            if refmsk[ilev][n, m]:
                                nb = nb + 1                    
            level = np.empty(nb, dtype=int)

        n     = np.empty(nb, dtype=int)
        m     = np.empty(nb, dtype=int)
        z     = np.full(nb, np.nan)
        self.nr_cells = nb

        if nlev == 1:
            ns = np.linspace(0, nmx[0] - 1, nmx[0], dtype=int)
            ms = np.linspace(0, mmx[0] - 1, mmx[0], dtype=int)
            m, n = np.meshgrid(ms, ns)
            n = np.transpose(n).flatten()
            m = np.transpose(m).flatten()

        else:    
            print("Setting cell indices ...")
            nb = 0
            for ilev in range(nlev):
                for mmm in range(mmx[ilev]):
                    for nnn in range(nmx[ilev]):
                            if refmsk[ilev][nnn, mmm]:
                                level[nb] = ilev
                                n[nb] = nnn
                                m[nb] = mmm
                                nb = nb + 1
        
        # We obtained all the n's, m's and levels. Now build the ugrid.
        print("Making XUGrid ...")
        ugrid2d = self.get_ugrid2d(n, m, level)
        self.data = xu.UgridDataset(grids=ugrid2d)

        attrs = {"x0": self.x0,
                 "y0": self.y0,
                 "nmax": self.nmax,
                 "mmax": self.mmax,
                 "dx": self.dx,
                 "dy": self.dy,
                 "rotation": self.rotation,
                 "nr_levels": self.nr_refinement_levels}
        self.data.attrs = attrs

        # Now add the data arrays
        self.data["crs"] = 0
        self.data["crs"].attrs = self.model.crs.to_cf()
        self.data["n"] = xu.UgridDataArray(xr.DataArray(data=n, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["m"] = xu.UgridDataArray(xr.DataArray(data=m, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["level"] = xu.UgridDataArray(xr.DataArray(data=level, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["z"] = xu.UgridDataArray(xr.DataArray(data=z, dims=[ugrid2d.face_dimension]), ugrid2d)
        # Set initial SFINCS mask to zeros
        mask = np.zeros(np.shape(z), dtype=np.int8)
        self.data["mask"] = xu.UgridDataArray(xr.DataArray(data=mask, dims=[ugrid2d.face_dimension]), ugrid2d)
        # Set initial SnapWave mask to zeros
        swmask = np.zeros(np.shape(z), dtype=np.int8)
        self.data["snapwave_mask"] = xu.UgridDataArray(xr.DataArray(data=swmask, dims=[ugrid2d.face_dimension]), ugrid2d)

        print("Number of cells : " + str(nb))
        print("Time elapsed : " + str(time.time() - start) + " s")

        self.find_neighbors()

        self.get_exterior()


    def find_neighbors(self):        

        print("Finding neighbors ...")

        start = time.time()

        n = self.data["n"].values[:] 
        m = self.data["m"].values[:] 
        # Initialize neighbor arrays
        # Set indices of neighbors to -1
        mu  = np.zeros(self.nr_cells, dtype=np.int8)
        mu1 = np.zeros(self.nr_cells, dtype=int) - 1
        mu2 = np.zeros(self.nr_cells, dtype=int) - 1
        md  = np.zeros(self.nr_cells, dtype=np.int8)
        md1 = np.zeros(self.nr_cells, dtype=int) - 1
        md2 = np.zeros(self.nr_cells, dtype=int) - 1
        nu  = np.zeros(self.nr_cells, dtype=np.int8)
        nu1 = np.zeros(self.nr_cells, dtype=int) - 1
        nu2 = np.zeros(self.nr_cells, dtype=int) - 1
        nd  = np.zeros(self.nr_cells, dtype=np.int8)
        nd1 = np.zeros(self.nr_cells, dtype=int) - 1
        nd2 = np.zeros(self.nr_cells, dtype=int) - 1
        nmx = np.zeros(self.nr_refinement_levels, dtype=int)

        if self.nr_refinement_levels == 1:
            # Regular grid
            nmax = n.max() + 1
            nms  = m*nmax + n
            for ic in range(self.nr_cells):
                # nd1
                nn = n[ic] - 1
                if nn >= 0:
                    mm = m[ic]
                    nm = mm*nmax + nn
                    j = binary_search(nms, nm)
                    if j is not None:
                        nd1[ic] = j
                # nu1
                nn = n[ic] + 1
                if nn < nmax:
                    mm = m[ic]
                    nm = mm*nmax + nn
                    j = binary_search(nms, nm)
                    if j is not None:
                        nu1[ic] = j
                # md1
                nn = n[ic]
                mm = m[ic] - 1
                nm = mm*nmax + nn
                j = binary_search(nms, nm)
                if j is not None:
                    md1[ic] = j
                # mu1
                nn = n[ic]
                mm = m[ic] + 1
                nm = mm*nmax + nn
                j = binary_search(nms, nm)
                if j is not None:
                    mu1[ic] = j
        else: 
            # Quadtree with refinement
            # Determine maximum n index for each level
            for ilev in range(self.nr_refinement_levels):
                ifirst = self.ifirst[ilev]
                # Now find index of last point in this level
                if ilev<self.nr_refinement_levels - 1:
                    ilast = self.ifirst[ilev + 1] - 1
                else:
                    ilast = self.nr_cells - 1
                ns  = n[ifirst:ilast + 1] # All the n indices in this level
                nmx[ilev] = ns.max()
            for ilev in range(self.nr_refinement_levels):
                # Find neighbors in same level
                # Index of first point in this level
                ifirst = self.ifirst[ilev]
                # Now find index of last point in this level
                if ilev<self.nr_refinement_levels - 1:
                    ilast = self.ifirst[ilev + 1] - 1
                else:
                    ilast = self.nr_cells - 1            
                nr = ilast - ifirst + 1         # number of cells in this level
                ns  = n[ifirst:ilast + 1] # All the n indices in this level
                ms  = m[ifirst:ilast + 1] # All the m indices in this level
                nms = ms*(nmx[ilev] + 1) + ns  # nm indices for this level
                
                for ic in range(nr):    
                    ib = ifirst + ic                
                    # Right
                    nm  = (m[ib] + 1)*(nmx[ilev] + 1) + n[ib]
                    j = binary_search(nms, nm)
                    if j is not None:
                        indxn = j + ifirst # index of neighbor
                        mu[ib]     = 0
                        mu1[ib]    = indxn
                        md[indxn]  = 0
                        md1[indxn] = ib                    
                    # Above (make sure we don't look neighbor in column to the right)
                    if n[ib] < nmx[ilev]:
                        nm  = m[ib]*(nmx[ilev] + 1) + n[ib] + 1
                        j = binary_search(nms, nm)
                        if j is not None:
                            indxn = j + ifirst # index of neighbor
                            nu[ib]     = 0
                            nu1[ib]    = indxn
                            nd[indxn]  = 0
                            nd1[indxn] = ib
                
                # Find neighbors in coarser level            
                if ilev>0:        
                    # Index of first point in the coarser level
                    ifirstc = self.ifirst[ilev - 1]
                    # Now find index of last point in the coarser level
                    ilastc = self.ifirst[ilev] - 1                
                    nsc  = n[ifirstc:ilastc + 1] # All the n indices in coarser level
                    msc  = m[ifirstc:ilastc + 1] # All the m indices in coarser level
                    nmxc = nmx[ilev - 1]
                    nmsc = msc*(nmxc + 1) + nsc             # nm indices for coarser level                
                    for ic in range(nr):                    
                        ib = ifirst + ic                    
                        # Only need to check if we haven't already found a neighbor at the same level
                        if mu1[ib]<0:                    
                            # Right
                            if odd(m[ib]):
                                if even(n[ib]):
                                    # Finer cell is the lower one
                                    nc  = int(n[ib]/2)
                                    mc  = int((m[ib] + 1) / 2)
                                    nmc = mc*(nmxc + 1) + nc
                                    j = binary_search(nmsc, nmc)
                                    if j is not None:
                                        indxn = j + ifirstc # index of neighbor
                                        mu[ib]     = -1
                                        mu1[ib]    = indxn
                                        md[indxn]  = 1
                                        md1[indxn] = ib
                                else:    
                                    # Finer cell is the upper one
                                    nc  = int((n[ib] - 1) / 2)
                                    mc  = int((m[ib] + 1) / 2)
                                    nmc = mc*(nmxc + 1) + nc
                                    j = binary_search(nmsc, nmc)
                                    if j is not None:
                                        indxn = j + ifirstc # index of neighbor
                                        mu[ib]     = -1
                                        mu1[ib]    = indxn
                                        md[indxn]  = 1
                                        md2[indxn] = ib                
                        if nu1[ib]<0:    
                            # Above
                            if odd(n[ib]):
                                if even(m[ib]):
                                    # Finer cell is the left one
                                    nc  = int((n[ib] + 1) / 2)
                                    if nc<=nmxc:
                                        mc  = int(m[ib]/2)
                                        nmc = mc*(nmxc + 1) + nc
                                        j = binary_search(nmsc, nmc)
                                        if j is not None:
                                            indxn = j + ifirstc # index of neighbor
                                            nu[ib]     = -1
                                            nu1[ib]    = indxn
                                            nd[indxn]  = 1
                                            nd1[indxn] = ib
                                else:    
                                    # Finer cell is the right one
                                    nc  = int((n[ib] + 1) / 2)
                                    if nc<=nmxc:
                                        mc  = int((m[ib] - 1) / 2)
                                        nmc = mc*(nmxc + 1) + nc
                                        j = binary_search(nmsc, nmc)
                                        if j is not None:
                                            indxn = j + ifirstc # index of neighbor
                                            nu[ib]     = -1
                                            nu1[ib]    = indxn
                                            nd[indxn]  = 1
                                            nd2[indxn] = ib

                # Find neighbors in finer level
                if ilev<self.nr_refinement_levels - 1:        
                    # Index of first point in the finer level
                    ifirstf = self.ifirst[ilev + 1]
                    # Now find index of last point in the finer level
                    if ilev<self.nr_refinement_levels - 2:                
                        ilastf = self.ifirst[ilev + 2] - 1
                    else:
                        ilastf = self.nr_cells - 1                
                    nsf  = n[ifirstf:ilastf + 1] # All the n indices in finer level
                    msf  = m[ifirstf:ilastf + 1] # All the m indices in finer level
                    nmxf = nmx[ilev + 1]
                    nmsf = msf*(nmxf + 1) + nsf        # nm indices for finer level
                    
                    for ic in range(nr):                    
                        ib = ifirst + ic
                        # Only need to check if we haven't already found a neighbor at the same level                        
                        if mu1[ib]<0:                    
                            # Right
                            # Finer cell is the lower one
                            nf  = int(n[ib]*2)
                            mf  = int((m[ib] + 1)*2)
                            nmf = mf*(nmxf + 1) + nf
                            j = binary_search(nmsf, nmf)
                            if j is not None:
                                indxn = j + ifirstf # index of neighbor
                                mu[ib]     = 1
                                mu1[ib]    = indxn
                                md[indxn]  = -1
                                md1[indxn] = ib
                            # Finer cell is the upper one
                            nf  = int(n[ib]*2) + 1
                            mf  = int((m[ib] + 1)*2)
                            nmf = mf*(nmxf + 1) + nf
                            j = binary_search(nmsf, nmf)
                            if j is not None:
                                indxn = j + ifirstf # index of neighbor
                                mu[ib]     = 1
                                mu2[ib]    = indxn
                                md[indxn]  = -1
                                md1[indxn] = ib

                        if nu1[ib]<0:                
                            # Above
                            # Finer cell is the left one
                            nf  = int((n[ib] + 1)*2)
                            if nf<=nmxf:
                                mf  = int(m[ib]*2)
                                nmf = mf*(nmxf + 1) + nf
                                j = binary_search(nmsf, nmf)
                                if j is not None:
                                    indxn = j + ifirstf # index of neighbor
                                    nu[ib]     = 1
                                    nu1[ib]    = indxn
                                    nd[indxn]  = -1
                                    nd1[indxn] = ib
                            # Finer cell is the right one
                            nf  = int((n[ib] + 1)*2)
                            if nf<=nmxf:
                                mf  = int(m[ib]*2) + 1
                                nmf = mf*(nmxf + 1) + nf
                                j = binary_search(nmsf, nmf)
                                if j is not None:
                                    indxn = j + ifirstf # index of neighbor
                                    nu[ib]     = 1
                                    nu2[ib]    = indxn               
                                    nd[indxn]  = -1
                                    nd1[indxn] = ib

        ugrid2d = self.data.grid
        self.data["nu"]  = xu.UgridDataArray(xr.DataArray(data=nu, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["nu1"] = xu.UgridDataArray(xr.DataArray(data=nu1, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["nu2"] = xu.UgridDataArray(xr.DataArray(data=nu2, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["nd"]  = xu.UgridDataArray(xr.DataArray(data=nd, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["nd1"] = xu.UgridDataArray(xr.DataArray(data=nd1, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["nd2"] = xu.UgridDataArray(xr.DataArray(data=nd2, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["mu"]  = xu.UgridDataArray(xr.DataArray(data=mu, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["mu1"] = xu.UgridDataArray(xr.DataArray(data=mu1, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["mu2"] = xu.UgridDataArray(xr.DataArray(data=mu2, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["md"]  = xu.UgridDataArray(xr.DataArray(data=md, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["md1"] = xu.UgridDataArray(xr.DataArray(data=md1, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["md2"] = xu.UgridDataArray(xr.DataArray(data=md2, dims=[ugrid2d.face_dimension]), ugrid2d)

        print("Time elapsed : " + str(time.time() - start) + " s")

    def set_bathymetry(self, bathymetry_sets, quiet=True):
        
        from cht.bathymetry.bathymetry_database import bathymetry_database

        if not quiet:
            print("Getting bathymetry data ...")

        nlev = self.nr_refinement_levels
        
        # Check if coordinates already exists
        xy = self.data.grid.face_coordinates
        zz = np.full(self.nr_cells, np.nan)
                        
        # Loop through all levels
        for ilev in range(nlev):

            if not quiet:
                print("Processing bathymetry level " + str(ilev + 1) + " of " + str(nlev) + " ...")
            
            ifirst = self.ifirst[ilev]
            if ilev<nlev - 1:
                ilast = self.ifirst[ilev + 1]
            else:
                ilast = self.nr_cells - 1
            
            # Make blocks off cells in this level only
            cell_indices_in_level = np.arange(ifirst, ilast + 1, dtype=int)
                  
            xz  = xy[cell_indices_in_level, 0]
            yz  = xy[cell_indices_in_level, 1]
            dxmin = self.dx/2**ilev

            zgl = bathymetry_database.get_bathymetry_on_points(xz,
                                                               yz,
                                                               dxmin,
                                                               self.model.crs,
                                                               bathymetry_sets)
            zz[cell_indices_in_level] = zgl

        ugrid2d = self.data.grid
        self.data["z"] = xu.UgridDataArray(xr.DataArray(data=zz, dims=[ugrid2d.face_dimension]), ugrid2d)

    def face_coordinates(self):
        # if self.data is None:
        #     return None, None
        xy = self.data.grid.face_coordinates
        return xy[:, 0], xy[:,1]

    def cut_inactive_cells(self):

        print("Removing inactive cells ...")

        n = self.data["n"].values[:]
        m = self.data["m"].values[:]
        level = self.data["level"].values[:]
        z = self.data["z"].values[:]
        mask = self.data["mask"].values[:]
        swmask = self.data["snapwave_mask"].values[:]

        indx = np.where((mask + swmask)>0)
            
        self.nr_cells = np.size(indx)
        n        = n[indx]
        m        = m[indx]
        level    = level[indx]
        z        = z[indx] 
        mask     = mask[indx]
        swmask   = swmask[indx]        

        # We obtained all the n's, m's and levels. Now build the ugrid.
        ugrid2d = self.get_ugrid2d(n, m, level)
        self.data = xu.UgridDataset(grids=ugrid2d)
        attrs = {"x0": self.x0,
                 "y0": self.y0,
                 "nmax": self.nmax,
                 "mmax": self.mmax,
                 "dx": self.dx,
                 "dy": self.dy,
                 "rotation": self.rotation,
                 "nr_levels": self.nr_refinement_levels}
        self.data.attrs = attrs

        # Now add the data arrays
        self.data["crs"] = 0
        self.data["crs"].attrs = self.model.crs.to_cf()
        self.data["n"] = xu.UgridDataArray(xr.DataArray(data=n, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["m"] = xu.UgridDataArray(xr.DataArray(data=m, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["level"] = xu.UgridDataArray(xr.DataArray(data=level, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["z"] = xu.UgridDataArray(xr.DataArray(data=z, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["mask"] = xu.UgridDataArray(xr.DataArray(data=mask, dims=[ugrid2d.face_dimension]), ugrid2d)
        self.data["snapwave_mask"] = xu.UgridDataArray(xr.DataArray(data=swmask, dims=[ugrid2d.face_dimension]), ugrid2d)

        self.find_neighbors()

        self.get_exterior()

    def get_ugrid2d(self, n, m, level):

        cosrot = np.cos(self.rotation*np.pi/180)
        sinrot = np.sin(self.rotation*np.pi/180)
        nlev = self.nr_refinement_levels
        nm_nodes   = np.full(4*self.nr_cells, 1e9, dtype=int)
        face_nodes = np.full((4, self.nr_cells), -1, dtype=int)
        node_x     = np.full(4*self.nr_cells, 1e9, dtype=float)
        node_y     = np.full(4*self.nr_cells, 1e9, dtype=float)
        ifac = []
        nmax = 0

        self.ifirst = np.zeros(self.nr_refinement_levels, dtype=int)
        last_lev = -1
        for ic in range(self.nr_cells):
            ilev = level[ic]
            if ilev>last_lev:
                # Found new level
                self.ifirst[ilev] = ic
                last_lev = ilev

        for ilev in range(nlev):
            ifac.append(2**(nlev - ilev - 1))
            i0 = self.ifirst[ilev]
            if ilev<nlev - 1:
                i1 = self.ifirst[ilev + 1]
            else:
                i1 = self.nr_cells    
            nmax = max(nmax, (np.amax(n[i0:i1]) + 1) * ifac[ilev])

        fac = 2**level
        ifac = 2**(nlev - level - 1)
        dxf = self.dx / 2**level
        dyf = self.dy / 2**level
        fac = 1

        tic = time.perf_counter()

        for icel in range(self.nr_cells):
            face_nodes[0, icel] = 4*icel
            face_nodes[1, icel] = 4*icel + 1
            face_nodes[2, icel] = 4*icel + 2
            face_nodes[3, icel] = 4*icel + 3

        ## Lower left
        nf = (n   )
        mf = (m   )
        nm_nodes[0:4*self.nr_cells:4] = ifac * (mf * (nmax + 1) + nf)
        node_x[0:4*self.nr_cells:4]   = self.x0 + cosrot*(mf*dxf) - sinrot*(nf*dyf)
        node_y[0:4*self.nr_cells:4]   = self.y0 + sinrot*(mf*dxf) + cosrot*(nf*dyf)
        ## Lower right
        nf = (n    )*fac
        mf = (m + 1)*fac
        nm_nodes[1:4*self.nr_cells:4] = ifac * (mf * (nmax + 1) + nf)
        node_x[1:4*self.nr_cells:4]   = self.x0 + cosrot*(mf*dxf) - sinrot*(nf*dyf)
        node_y[1:4*self.nr_cells:4]   = self.y0 + sinrot*(mf*dxf) + cosrot*(nf*dyf)
        ## Upper right
        nf = (n + 1)*fac
        mf = (m + 1)*fac
        nm_nodes[2:4*self.nr_cells:4] = ifac * (mf * (nmax + 1) + nf)
        node_x[2:4*self.nr_cells:4]   = self.x0 + cosrot*(mf*dxf) - sinrot*(nf*dyf)
        node_y[2:4*self.nr_cells:4]   = self.y0 + sinrot*(mf*dxf) + cosrot*(nf*dyf)
        ## Upper left
        nf = (n + 1)*fac
        mf = (m   )*fac
        nm_nodes[3:4*self.nr_cells:4] = ifac * (mf * (nmax + 1) + nf)
        node_x[3:4*self.nr_cells:4]   = self.x0 + cosrot*(mf*dxf) - sinrot*(nf*dyf)
        node_y[3:4*self.nr_cells:4]   = self.y0 + sinrot*(mf*dxf) + cosrot*(nf*dyf)

        toc = time.perf_counter()
        print(f"Found nodes in {toc - tic:0.4f} seconds")

        # Get rid of duplicates
        tic = time.perf_counter()

        xxx, indx, irev = np.unique(nm_nodes, return_index=True, return_inverse=True)
        node_x = node_x[indx]
        node_y = node_y[indx]

        for icel in range(self.nr_cells):
            for j in range(4):
                face_nodes[j, icel] = irev[face_nodes[j, icel]]

        toc = time.perf_counter()
        print(f"Get rid of duplicates {toc - tic:0.4f} seconds")

        nodes = np.transpose(np.vstack((node_x, node_y)))
        faces = np.transpose(face_nodes)
        fill_value = -1

        ugrid2d = xu.Ugrid2d(nodes[:, 0], nodes[:, 1], fill_value, faces)
        ugrid2d.set_crs(self.model.crs)

        # Set datashader df to None
        self.df = None 


        return ugrid2d

    def get_exterior(self):
        indx = self.data.grid.edge_node_connectivity[self.data.grid.exterior_edges, :]
        x = self.data.grid.node_x[indx]
        y = self.data.grid.node_y[indx]
        # Make linestrings from numpy arrays x and y
        linestrings = [shapely.LineString(np.column_stack((x[i], y[i]))) for i in range(len(x))]
        # Merge linestrings
        merged = shapely.ops.linemerge(linestrings)
        # Merge polygons
        polygons = shapely.ops.polygonize(merged)
#        polygons = shapely.simplify(polygons, self.dx)
        self.exterior = gpd.GeoDataFrame(geometry=list(polygons), crs=self.model.crs)

    def get_datashader_dataframe(self):
        # Create a dataframe with line elements
        x1 = self.data.grid.edge_node_coordinates[:,0,0]
        x2 = self.data.grid.edge_node_coordinates[:,1,0]
        y1 = self.data.grid.edge_node_coordinates[:,0,1]
        y2 = self.data.grid.edge_node_coordinates[:,1,1]
        transformer = Transformer.from_crs(self.model.crs,
                                            3857,
                                            always_xy=True)
        x1, y1 = transformer.transform(x1, y1)
        x2, y2 = transformer.transform(x2, y2)
        self.df = pd.DataFrame(dict(x1=x1, y1=y1, x2=x2, y2=y2))

    def map_overlay(self, file_name, xlim=None, ylim=None, color="black", width=800):
        if self.data is None:
            # No grid (yet)
            return False
        if not hasattr(self, "df"):
            self.df = None
        if self.df is None: 
            self.get_datashader_dataframe()

        transformer = Transformer.from_crs(4326,
                                    3857,
                                    always_xy=True)
        xl0, yl0 = transformer.transform(xlim[0], ylim[0])
        xl1, yl1 = transformer.transform(xlim[1], ylim[1])
        xlim = [xl0, xl1]
        ylim = [yl0, yl1]
        ratio = (ylim[1] - ylim[0]) / (xlim[1] - xlim[0])
        height = int(width * ratio)
        cvs = ds.Canvas(x_range=xlim, y_range=ylim, plot_height=height, plot_width=width)
        agg = cvs.line(self.df, x=['x1', 'x2'], y=['y1', 'y2'], axis=1)
        img = tf.shade(agg)
        path = os.path.dirname(file_name)
        name = os.path.basename(file_name)
        name = os.path.splitext(name)[0]
        export_image(img, name, export_path=path)
        return True

    def read(self, file_name=None):
        if file_name == None:
            if not self.model.input.variables.qtrfile: 
                self.model.input.variables.qtrfile = "sfincs.nc"
            file_name = os.path.join(self.model.path, self.model.input.variables.qtrfile)
        self.data = xu.open_dataset(file_name)
        self.data.close()
        self.nr_cells = self.data.dims['mesh2d_nFaces']
        self.get_exterior()
        crd_dict = self.data["crs"].attrs
        if "projected_crs_name" in crd_dict:
            self.model.crs = CRS(crd_dict["projected_crs_name"])
        elif "geographic_crs_name" in crd_dict:
            self.model.crs = CRS(crd_dict["geographic_crs_name"])
        else:
            print("Could not find CRS in quadtree netcdf file")    

    def write(self, file_name=None, version=0):
        if file_name == None:
            if not self.model.input.variables.qtrfile: 
                self.model.input.variables.qtrfile = "sfincs.nc"
            file_name = os.path.join(self.model.path, self.model.input.variables.qtrfile)
        attrs = self.data.attrs
        ds = self.data.ugrid.to_dataset()
        ds.attrs = attrs
        ds.to_netcdf(file_name)

    def make_index_tiles(self, path, zoom_range=None, format=0):
        
        import math
        from cht.tiling.tiling import deg2num
        from cht.tiling.tiling import num2deg
        import cht.misc.fileops as fo
        
        npix = 256
        
        if not zoom_range:
            zoom_range = [0, 13]

        cosrot = math.cos(-self.rotation*math.pi/180)
        sinrot = math.sin(-self.rotation*math.pi/180)       

        # Compute lon/lat range
        xmin = np.amin(self.x) - 10*self.dx
        xmax = np.amax(self.x) + 10*self.dx
        ymin = np.amin(self.y) - 10*self.dy
        ymax = np.amax(self.y) + 10*self.dy
        transformer = Transformer.from_crs(self.crs,
                                            CRS.from_epsg(4326),
                                            always_xy=True)
        lon_min, lat_min = transformer.transform(xmin, ymin)
        lon_max, lat_max = transformer.transform(xmax, ymax)
        lon_range = [lon_min, lon_max]
        lat_range = [lat_min, lat_max]        
        
        transformer_a = Transformer.from_crs(CRS.from_epsg(4326),
                                                CRS.from_epsg(3857),
                                                always_xy=True)
        transformer_b = Transformer.from_crs(CRS.from_epsg(3857),
                                                self.crs,
                                                always_xy=True)
        
        i0_lev = []
        i1_lev = []
        nmax_lev = []
        mmax_lev = []
        nm_lev = []
        for level in range(self.nr_refinement_levels):
            i0 = self.level_index[level]
            if level<self.nr_refinement_levels - 1:
                i1 = self.level_index[level + 1]
            else:
                i1 = self.nr_cells   
            i0_lev.append(i0)    
            i1_lev.append(i1)    
            nmax_lev.append(np.amax(self.n[i0:i1]) + 1)
            mmax_lev.append(np.amax(self.m[i0:i1]) + 1)
            mm = self.m[i0:i1]
            nn = self.n[i0:i1]
            nm_lev.append(mm*nmax_lev[level] + nn)

        for izoom in range(zoom_range[0], zoom_range[1] + 1):
            
            print("Processing zoom level " + str(izoom))
        
            zoom_path = os.path.join(path, str(izoom))
        
            dxy = (40075016.686/npix) / 2 ** izoom
            xx = np.linspace(0.0, (npix - 1)*dxy, num=npix)
            yy = xx[:]
            xv, yv = np.meshgrid(xx, yy)
        
            ix0, iy0 = deg2num(lat_range[0], lon_range[0], izoom)
            ix1, iy1 = deg2num(lat_range[1], lon_range[1], izoom)
        
            for i in range(ix0, ix1 + 1):
            
                path_okay = False
                zoom_path_i = os.path.join(zoom_path, str(i))
            
                for j in range(iy0, iy1 + 1):
            
                    file_name = os.path.join(zoom_path_i, str(j) + ".dat")
            
                    # Compute lat/lon at ll corner of tile
                    lat, lon = num2deg(i, j, izoom)
            
                    # Convert to Global Mercator
                    xo, yo   = transformer_a.transform(lon,lat)
            
                    # Tile grid on local mercator
                    x = xv[:] + xo + 0.5*dxy
                    y = yv[:] + yo + 0.5*dxy
            
                    # Convert tile grid to crs of SFINCS model
                    x, y = transformer_b.transform(x, y)

                    # Now rotate around origin of SFINCS model
                    x00 = x - self.x0
                    y00 = y - self.y0
                    xg  = x00*cosrot - y00*sinrot
                    yg  = x00*sinrot + y00*cosrot

                    indx = np.full((npix, npix), -999, dtype=int)

                    for ilev in range(self.nr_refinement_levels):
                        nmax = nmax_lev[ilev]
                        mmax = mmax_lev[ilev]
                        i0   = i0_lev[ilev]
                        i1   = i1_lev[ilev]
                        dx   = self.dx/2**ilev
                        dy   = self.dy/2**ilev
                        iind = np.floor(xg/dx).astype(int)
                        jind = np.floor(yg/dy).astype(int)
                        # Now check whether this cell exists on this level
                        ind  = iind*nmax + jind
                        ind[iind<0]   = -999
                        ind[jind<0]   = -999
                        ind[iind>=mmax] = -999
                        ind[jind>=nmax] = -999

                        ingrid = np.isin(ind, nm_lev[ilev], assume_unique=False) # return boolean for each pixel that falls inside a grid cell
                        incell = np.where(ingrid)                                # tuple of arrays of pixel indices that fall in a cell

                        if incell[0].size>0:
                            # Now find the cell indices
                            try:
                                cell_indices = np.searchsorted(nm_lev[ilev], ind[incell[0], incell[1]]) + i0_lev[ilev]
                                indx[incell[0], incell[1]] = cell_indices
                            except:
                                pass

                    if np.any(indx>=0):                        
                        if not path_okay:
                            if not os.path.exists(zoom_path_i):
                                fo.mkdir(zoom_path_i)
                                path_okay = True
                                
                        # And write indices to file
                        fid = open(file_name, "wb")
                        fid.write(indx)
                        fid.close()

    


def get_neighbors_in_larger_cell(n, m):    
    nnbr = [-1, -1, -1, -1]
    mnbr = [-1, -1, -1, -1]
    if not odd(n) and not odd(m):
        # lower left
        nnbr[0] = n + 1
        mnbr[0] = m
        nnbr[1] = n
        mnbr[1] = m + 1
        nnbr[2] = n + 1
        mnbr[2] = m + 1
    elif not odd(n) and odd(m):
        # lower right
        nnbr[1] = n
        mnbr[1] = m - 1
        nnbr[2] = n + 1
        mnbr[2] = m - 1
        nnbr[3] = n + 1
        mnbr[3] = m
    elif odd(n) and not odd(m):
        # upper left
        nnbr[1] = n - 1
        mnbr[1] = m
        nnbr[2] = n - 1
        mnbr[2] = m + 1
        nnbr[3] = n
        mnbr[3] = m + 1
    else:
        # upper right
        nnbr[1] = n - 1
        mnbr[1] = m - 1
        nnbr[2] = n - 1
        mnbr[2] = m
        nnbr[3] = n
        mnbr[3] = m - 1    
    return nnbr,mnbr

def odd(num):
    if (num % 2) == 1:  
        return True
    else:  
        return False

def even(num):
    if (num % 2) == 0:  
        return True
    else:  
        return False

def inpolygon(xq, yq, p):
    shape = xq.shape
    xq = xq.reshape(-1)
    yq = yq.reshape(-1)
#    xv = xv.reshape(-1)
#    yv = yv.reshape(-1)
    q = [(xq[i], yq[i]) for i in range(xq.shape[0])]
#    q = [Point(xq[i], yq[i]) for i in range(xq.shape[0])]
#    mp = MultiPoint(q)
    p = path.Path([(crds[0], crds[1]) for i, crds in enumerate(p.exterior.coords)])
#    p = path.Path([(xv[i], yv[i]) for i in range(xv.shape[0])])
    return p.contains_points(q).reshape(shape)
#    return mp.within(p)

def binary_search(vals, val):    
    indx = np.searchsorted(vals, val)
    if indx<np.size(vals):
        if vals[indx] == val:
            return indx
    return None

def gdf2list(gdf_in):
   gdf_out = []
   for feature in gdf_in.iterfeatures():
      gdf_out.append(gpd.GeoDataFrame.from_features([feature]))
   return gdf_out
