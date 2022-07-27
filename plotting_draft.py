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



def starplot(star_name, ax):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*raw.dat')
    color_dict = {'562': 'C2', '832': 'C3', '466': 'C0', '716': 'C1' } 
    for i, file_star_name in enumerate(finder):
        if file_star_name.endswith('raw.dat'):
            fname = finder[i]
            edited_fname = os.path.expanduser(fname)
            filter_num = fname.split('_')[-2]  
            dat = at.read(edited_fname)
    
            #gathering all information necessary to plot data
            ax.plot(dat['ann_center'], dat['delta_mag_limit'], label=f'{filter_num} nm', 
                    color = color_dict[filter_num], alpha = 0.5)     
            
  
def one_star(star_name):
    ax = plt.subplot()
    ax.set_xlabel('Separation [arcsec]')
    ax.set_ylabel('Delta Mag')
    ax.set_title(star_name)
    starplot(star_name, ax)
    ax.legend()    

#define new function , define figure use for loop to call starplot for all stars
# def all_star_plot(star_name):
#     # for star_name in #new finder:
#     #     one_star(star_name)
#     pass
        


if __name__== "__main__":
    star_name = "IC2602b104256-6355"
    one_star(star_name)
    
