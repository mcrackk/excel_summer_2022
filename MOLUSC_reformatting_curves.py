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


# star_name = "IC2602b104422-6415" 

# location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
# location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
# finder = glob.glob(f'{location_and_name}*raw.dat') 
# for i, file_star_name in enumerate(finder):
#     if file_star_name.endswith('raw.dat'):
#         fname = finder[i]
#         edited_fname = os.path.expanduser(fname)
#         dat = at.read(edited_fname)
#         data_table = Table(data = [dat['ann_center'], dat['delta_mag_limit']], names=["Separation", "Delta Mag"])
#         print(data_table)

# format of files originally was "cluster_star_obsdate_filter" and the raw/fit.dat was added later
#instead of worrying about the names of the filters, you can do this:
    # filename.replace(".dat", "MOLUSC.dat)
    # and it should have that name for every file
    
    
star_name = "IC2602b104422-6415" 

location =  "Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
location_and_name = os.path.join(os.path.expanduser(f"~/{location}"), star_name)
finder = glob.glob(f'{location_and_name}*.dat') 
print(finder)
for i, file_star_name in enumerate(finder):
    if file_star_name.endswith('.dat'):
        fname = finder[i]
        edited_fname = os.path.expanduser(fname)
        dat = at.read(edited_fname)
        data_table = Table(data = [dat['ann_center'], dat['delta_mag_limit']], names=["Separation", "Delta Mag"])
        print(data_table)
        MOLUSC_fname = edited_fname.replace(".dat", "MOLUSC.dat")
        print(MOLUSC_fname)