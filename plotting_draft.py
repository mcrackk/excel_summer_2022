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


color_dict = {'562': '#dede00', '832': '#e41a1c', '466': '#377eb8', '716': '#f781bf' }
def starplot(star_name, ax):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*raw.dat') 
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


def all_star_plot(star_names):
    ax = plt.subplot()
    ax.set_xlabel('Separation [arcsec]')
    ax.set_ylabel('Delta Mag')
    ax.set_title("All Zorro Targets")
    filter_nums = [832, 716, 562, 466]
    for filter_num in filter_nums:
        ax.plot([], [], label=f'{filter_num} nm', 
                color = color_dict[str(filter_num)], alpha = 1)
    ax.legend()
    for star_name in star_names:
          print(star_name)
          starplot(star_name, ax)
    plt.savefig("all_zorro_targets_pyplot")   
# save plot with with useful name (make note in lab motebook refer to script and location), remake same plot but with fitted curves
# put filter curves into MOLUSC format (in a new .py file!!!)
#       create a new table for each star with the specified format and write out to files   
#       create unique file name for each star 
#       start with one star and build it up to genealize it (use at.read and at.write)


if __name__== "__main__":
    # star_name = "IC2602b104256-6355"
    # one_star(star_name)
    
    

    star_names = at.read("all_zorro_targets.csv")
    all_star_plot(star_names['name'])
    
