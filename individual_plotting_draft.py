#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 11:27:19 2022

@author: kiramccracken
"""

import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as at

ssfont = {'fontname':'sans-serif'}
color_dict = {'562': '#984ea3', '832': '#e41a1c', '466': '#999999', '716': '#f781bf' }

def starplot(star_name, ax):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*fit.dat') 
    for i, file_star_name in enumerate(finder):
        if file_star_name.endswith('fit.dat'):
            fname = finder[i]
            edited_fname = os.path.expanduser(fname)
            filter_num = fname.split('_')[-2]  
            if (float(filter_num) > 700):
                edited_fname_red = edited_fname
            else:
                continue
            dat = at.read(edited_fname_red)
            #gathering all information necessary to plot data
            
            ax.plot(dat['ann_center'], dat['delta_mag_limit'], label=f'{filter_num} nm', 
                    color = color_dict[filter_num], alpha = 0.5)     
            
  
def one_star(star_name):
    ax = plt.subplot()
    ax.set_xlabel('Separation [arcsec]', **ssfont)
    ax.set_ylabel('Delta Mag', **ssfont)
    ax.set_ylim(10, -0.5)
    ax.set_title(star_name, **ssfont)
    starplot(star_name, ax)
    #ax.plot()  plot the individual point here !!!!
    ax.legend()    

one_star("IC2602b104256-6355")