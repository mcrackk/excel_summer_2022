#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:04:05 2022

@author: kiramccracken
"""

#imports!!!
#glob to get list of all of raw files
#create empty list that will hold star names
#loop over all files
#split file name to extract star name only
#append star name to list if not already there

#write all names to new file

import glob
import os
import numpy as np
import astropy.io.ascii as at

location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
location_expanded= os.path.join(os.path.expanduser(f"~/{location}"))
find_all_stars = glob.glob(f'{location_expanded}*raw.dat')
name_list = []
for name in find_all_stars:
    starname = name.split('/')[8].split('_')[-4]
    name_list.append(starname)
unique_names = np.unique(name_list)
print(unique_names)

out_names = {"name": unique_names}
at.write(out_names, "all_zorro_targets.csv", delimiter = ",")


    
    
