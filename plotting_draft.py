#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:12:26 2022

@author: kiramccracken
"""
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as at



def starplot(star_name):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    #expanded_location = os.path.expanduser(location)
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    #print(location_and_name)
    fname1=f"{location_and_name}_562_raw.dat"
    fname2=f"{location_and_name}_832_raw.dat"
    edited_fname1 = os.path.expanduser(fname1)
    edited_fname2 = os.path.expanduser(fname2)
    filter1 = fname1.split('_')[-2]
    filter2 = fname2.split('_')[-2]
    dat1 = at.read(edited_fname1)
    dat2 = at.read(edited_fname2)

    #gathering all information necessary to plot data

    plt.plot(dat1['ann_center'], dat1['delta_mag_limit'], 'k', label=f'{filter1} nm')
    plt.plot(dat2['ann_center'], dat2['delta_mag_limit'], 'r', label=f'{filter2} nm')
    plt.xlabel('Separation [arcsec]')
    plt.ylabel('Delta Mag')
    plt.legend()
    #creating plot
    
    finder = glob.glob(f'{location_and_name}*raw.dat')
    print(finder)




if __name__== "__main__":
    star_name = "IC2391b084426-5242_20190522"
    starplot(star_name)