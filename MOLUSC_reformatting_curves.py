#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:44:58 2022

@author: kiramccracken
"""

import numpy as np
import astropy.io.ascii as at
from astropy.table import Table
import os
import glob


    
    
star_name = "IC2602b104422-6415" 

#multiply separation column by 1000 cuz milliarcseconds 


        
def one_star_table(star_name):
    location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
    location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
    finder = glob.glob(f'{location_and_name}*.dat') 
    for i, file_star_name in enumerate(finder):
        if file_star_name.endswith('.dat'):
            edited_fname = os.path.expanduser(file_star_name)
            dat = at.read(edited_fname)
            dat['ann_center'] = dat['ann_center']*1000
            data_table = Table(data = [dat['ann_center'], dat['delta_mag_limit']], names=["Sep", "Contrast"])
            
            print(data_table)
            MOLUSC_fname = edited_fname.replace(".dat", "MOLUSC.dat")
            new_pathname = MOLUSC_fname.replace('Zorro_data_reformatted', 'Zorro_to_MOLUSC')
            at.write(data_table, new_pathname, overwrite = True)
                

star_names = at.read("all_zorro_targets.csv")

 

  
def every_star_table(star_names):
    for star_name in star_names:
        one_star_table(star_name)
 
 
every_star_table(star_names['name'])




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
