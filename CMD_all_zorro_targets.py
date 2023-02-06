#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:00:34 2022

@author: kiramccracken
"""


import numpy as np
import astropy.io.ascii as at
from astropy.table import Table
import matplotlib.pyplot as plt
import os
import glob

#TASKS!!!
#cluster members color should be gray DONE; highlighting stars that we actually targeted 
#add to plot_one_cluster; look up matplotlib keywords "alpha" DONE and "zorder" 
#plot things that are gemini_obs in csv files !!!
#review numpy quickstart and astropy table tut to figure out how to turn true or false columns into highlighted points

color_dict = {'group' : '#999999', 'obs': '#e41a1c'}

def plot_one_cluster(cluster_name, ax):
    data_location = "Google Drive/Shared drives/DouglasGroup/data/Zorro_speckle_info/" 
    data_location_expand = os.path.join(os.path.expanduser(f"~/{data_location}"))
    cluster_file = f"all_{cluster_name}_forKira.csv"
    fname = os.path.join(f"{data_location_expand}", f"{cluster_file}")
    #only use ~/ for expanduser !!!
    

    data_table = at.read(fname)
    
    dmod = 5-5*np.log10(data_table["dist"])
    abs_g = data_table['GAIAEDR3_G'] + dmod
    ax.plot(data_table['GAIAEDR3_BP']-data_table['GAIAEDR3_RP'], abs_g,
        'o', alpha=0.1, markersize=7, color = color_dict['group'])
    
    obs = data_table['gemini_obs']=="True"
    
   
    ax.plot(data_table['GAIAEDR3_BP'][obs]-data_table['GAIAEDR3_RP'][obs], abs_g[obs],
            '^', alpha=1, markersize=7,color = color_dict['obs'], zorder=2.5)
    
     


def all_cluster_CMD():
    
    ax = plt.subplot()
    ax.set_xlabel("Bp-Rp")
    ax.set_ylabel("Absolute G Mag")
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(14, -2)
    #ax.set_title("Absolute G Magnitude vs. Bp-Rp")
    ax.grid(axis='both')
    
    
    ax.plot([], [], '^', label='With Speckle Data', color=color_dict['obs'])
    ax.plot([], [], 'o', label='All Members', color=color_dict['group'])
       
        
    ax.legend()
    
    cluster_list = ["IC_2602", "IC_2391", "Collinder_135", "NGC_2547", "NGC_2451A"]
    for cluster_name in cluster_list: 
        plot_one_cluster(cluster_name, ax)
        
    

if __name__== "__main__":
   
    all_cluster_CMD()








