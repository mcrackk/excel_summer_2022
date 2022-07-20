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
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*raw.dat')
    fname1= finder[0]
    fname2= finder[1]
    edited_fname1 = os.path.expanduser(fname1)
    edited_fname2 = os.path.expanduser(fname2)
    filter1 = fname1.split('_')[-2]
    filter2 = fname2.split('_')[-2]
    print(filter2)
    ####So now you have to make sure you can pull the filter numbers so that you can use them below and 
    ####make the legend in lines 33, 34 and 37
    dat1 = at.read(edited_fname1)
    dat2 = at.read(edited_fname2)

    #gathering all information necessary to plot data

    plt.plot(dat1['ann_center'], dat1['delta_mag_limit'], 'k', label=f'{filter1} nm')
    plt.plot(dat2['ann_center'], dat2['delta_mag_limit'], 'r', label=f'{filter2} nm')
    plt.xlabel('Separation [arcsec]')
    plt.ylabel('Delta Mag')
    plt.legend()
    
    


if __name__== "__main__":
    star_name = "IC2391b084426-5242_20190522"
    starplot(star_name)