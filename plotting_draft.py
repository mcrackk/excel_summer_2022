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
    print(finder)
    for i, star_name in enumerate(finder):
        if star_name.endswith('raw.dat'):
            fname = finder[i]
            #print(finder)
            #print(finder[i])
            edited_fname = os.path.expanduser(fname)
            filter_ = fname.split('_')[-2]  
            dat = at.read(edited_fname)
    
            #gathering all information necessary to plot data
    
            plt.plot(dat['ann_center'], dat['delta_mag_limit'], label=f'{filter_} nm')
    plt.xlabel('Separation [arcsec]')
    plt.ylabel('Delta Mag')
    plt.legend()
  
            
            
           


if __name__== "__main__":
    star_name = "IC2391b084426-5242_"
    starplot(star_name)