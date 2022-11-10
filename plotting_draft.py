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


color_dict = {'562': '#984ea3', '832': '#e41a1c', '466': '#999999', '716': '#f781bf', 'halpha': '#984ea3'}
def starplot(star_name, ax):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*fit.dat') 
    for i, file_star_name in enumerate(finder):
        if file_star_name.endswith('fit.dat'):
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
    ax.invert_yaxis()
    ax.set_ylabel('Delta Mag')
    ax.set_title(star_name)
    starplot(star_name, ax)
    ax.legend()    


def all_star_plot(star_names):
    ax = plt.subplot()
    ax.set_xlabel('Separation [arcsec]')
    #ax.set_ylim(top=10)
    #ax.invert_yaxis()
    ax.set_ylim(10, -0.5)
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


if __name__== "__main__":
    # star_name = "IC2602b104256-6355"
    # one_star(star_name)
    
    

    star_names = at.read("all_zorro_targets.csv")
    all_star_plot(star_names['name'])

binary_location = "Google Drive/Shared drives/DouglasGroup/data/Zorro_speckle_info/Douglas_Binaries_GS_all.txt"
binary_location_expanded = os.path.join(os.path.expanduser(f"~/{binary_location}"))



def binary_detections(all_names):
    ssfont = {'fontname':'sans-serif'}
    color_dict = {'purple 1': '#984ea3', 'red': '#e41a1c', 'grey': '#999999', 'pink': '#f781bf' }

    
    #on same plot with the curves 
    #for confirmed_pair in binary_location_expanded:
    #for name in binary_location_expanded:
    data = at.read(binary_location_expanded)
#print(data)
    ax = plt.subplot()
    ax.plot(data['rho'][1:], data['delm'][1:], 'o', alpha = 1, color = color_dict['red'])
    ax.set_xlabel("Separation [arcsec]")
    ax.set_ylabel("Delta mag")
    ax.set_ylim(10, -0.5)
    ax.set_xlim(-0.04, 1.2)


if __name__=="__main__":
    
    all_names = at.read(binary_location_expanded)
    binary_detections(all_names['ID'])


