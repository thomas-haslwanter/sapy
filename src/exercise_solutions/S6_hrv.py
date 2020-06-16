""" Solution Exercise 'Heart Rate Variability', Chapter 'Events'

Estimation of hear beat variability 
To read in the data, you need the package 'wfdb'
"""

# author:   Thomas Haslwanter
# date:     June-2020

import numpy as np
import matplotlib.pyplot as plt
import os
import wfdb

# Set the parameters
data_dir = '../../data'
in_file = 'rec_1'
rate = 500          # [Hz]
nn = 10             # calculate HRV over nn heart beats

# Import the data
os.chdir(data_dir)
sig, fields = wfdb.rdsamp(in_file)
ecg = sig[:,0]
plt.plot(ecg)

# Set the threshold for R-detection
#threshold = plt.ginput(1)
threshold = 0.4

# Find the locations where the signal exceeds the threshold
high = ecg>threshold
onset = np.where(np.diff(high*1.)==1)[0]

# Times between two heartbeats
dt = 1/rate
dts = np.diff(onset)*dt

# Calculate the variability, over nn heartbeats
sds = []
for ii in range(len(dts)-nn):
    sds.append(np.std(dts[ii:ii+nn]))
    
# Print minimum and maximum variability    
print(f'Minimum HRV: {np.min(sds):6.3f}')
print(f'Maximum HRV: {np.max(sds):6.3f}')




    
