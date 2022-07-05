# Import additional packages here
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as at

# Look up the os.path package and edit filenames to use os.path.expanduser 
#Done
# define the object name to run
#Done
# use f string formatting to include it in the filename
#Done
# Bonus 1: Separate the directory (up through Zorro_data_reformatted) from the individual files
# and link them into the full filename using os.path.join

# Bonus 2: use the data directory and object name to search for files using glob.glob



star_name = "IC2391b084426-5242_20190522"
location =  "/Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/"
location_and_name = os.path.join(location, star_name)
fname1=f"~{location_and_name}_562_raw.dat"
fname2=f"~{location_and_name}_832_raw.dat"
edited_fname1 = os.path.expanduser(fname1)
edited_fname2 = os.path.expanduser(fname2)
filter1 = fname1.split('_')[-2]
filter2 = fname2.split('_')[-2]
dat1 = at.read(edited_fname1)
dat2 = at.read(edited_fname2)

plt.plot(dat1['ann_center'], dat1['delta_mag_limit'], 'k', label=f'{filter1} nm')
plt.plot(dat2['ann_center'], dat2['delta_mag_limit'], 'r', label=f'{filter2} nm')
plt.xlabel('Separation [arcsec]')
plt.ylabel('Delta Mag')
plt.legend()



finder = glob.glob(os.path.join(r"~/Google Drive/Shared drives/DouglasGroup/data/Zorro_data_reformatted/IC2391b084426-5242_20190522_562_fit.dat"))
print(finder)

# I initially tried to do an f string with the "location_and_name" and adding "*raw.dat" to specify I wanted all files ending in raw.dat using the syntax for
#glob.glob but alas it didn't work
