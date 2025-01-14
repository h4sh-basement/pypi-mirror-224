# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:25:56 2021

@author: ormondt
"""
import datetime
import pandas as pd

from cht.tide.tide import Tide
import cht.tide.constituent as cons

def predict(data, start=None, end=None, freq=None, times=None, format="dataframe"):

    # Times can be defined with pandas date_ranges "times", or by datetime-like object start, stop, and freq

    if times is None:
        if not freq:
            freq = datetime.timedelta(minutes=10)
        times = pd.date_range(start=start, end=end, freq=freq)

    all_constituents = [c for c in cons.noaa if c != cons._Z0]
    
    constituents=[]
    for name in data.index.to_list():
        if name == "MM":
            name = "Mm"
        if name == "MF":
            name = "Mf"
        if name == "SA":
            name = "Sa"
        if name == "SSA":
            name = "Ssa"
        if name == "MU2":
            name = "mu2"
        if name == "NU2":
            name = "nu2"
        for cnst in all_constituents:
            if cnst.name == name:
                constituents.append(cnst)
                continue
    
    td=Tide(constituents=constituents,
            amplitudes=data.iloc[:,0].to_list(),
            phases=data.iloc[:,1].to_list())
    v=td.at(times)

    if format == "dataframe":
        df = pd.DataFrame(times, columns=['time'])
        df["water_level"] = v
        return df
    else:    
        return v
