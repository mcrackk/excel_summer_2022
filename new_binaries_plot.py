#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:15:16 2022

@author: kiramccracken
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as at


#host_name = "IC2391b084300-5354"

ssfont = {'fontname':'sans-serif'}
color_dict = {'purple 1': '#984ea3', 'red': '#e41a1c', 'grey': '#999999', 'pink': '#f781bf' }

binary_location = "Google Drive/Shared drives/DouglasGroup/data/Zorro_speckle_info/Douglas_Binaries_GS_all.txt"
binary_location_expanded = os.path.join(os.path.expanduser(f"~/{binary_location}"))
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
ax.set_xlim(0, 1.2)
 