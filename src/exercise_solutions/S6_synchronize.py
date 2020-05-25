"""Solution Chapter 6: Events

Synchronize the acceleration measurements from two datasets
The information about the measurement units is taken from the column names
"""

# author:   Thomas Haslwanter
# date:     May-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Get the data
data_dir = r'..\..\Data'
in_mobile = 'mobile_phone.txt'
in_imu = 'ngimu.txt'
rate_sync = 100         # [Hz] for synchronized data

# ... mobile phone data
os.chdir(data_dir)
mobile = pd.read_csv(in_mobile,
                     sep='\t',
                     names=['time', 'acc_x', 'acc_y', 'acc_z', 'total'],
                     dtype='float',
                     skiprows=1,
                     decimal=',')

# ... imu data
# Make sure that the 'time' column and the 'acceleration' columns have the same
# name as the ones from the mobile phone, so they can be processed in a loop
imu = pd.read_csv(in_imu)
imu.columns = ['time',
               'w_x', 'w_y', 'w_z',
               'acc_x', 'acc_y', 'acc_z',
               'b_x', 'b_y', 'b_z',
               'p']
# For the imus-values, the acceleration is given in units of 'g'
imu.iloc[:, 4:7] *= 9.81

# Trigger on the 'total' acceleration. For the 'mobile', we already have it
imu_acc = imu.filter(regex='acc*')
imu['total'] = np.sqrt(np.sum(imu_acc**2, axis=1))

ip_ed = []      # store the interpolated data ...
for sensor in ['mobile', 'imu']:
    df = eval(sensor)
    df_new = pd.DataFrame()         # ... in a DataFrame
    start = np.argmax(df.total)     # Point of max acc
    t_int = np.arange(df.time[start], df.time.iloc[-1], 1/rate_sync)
    
    df_new['time']  = t_int-t_int[0]    # Set this point to '0'
    # For (x/y/z)
    df_acc = df.filter(regex='acc*')
    for col in df_acc.columns:
        df_new['_'.join([sensor, col])] = np.interp(t_int, df.time, df_acc[col])
    ip_ed.append(df_new)
    
# Chop off the longer one    
t_max = np.max([ip_ed[0].time.iloc[-1], ip_ed[1].time.iloc[-1]])
for sensor in ip_ed:
    sensor = sensor.drop(sensor[sensor.time > t_max].index)
    
ip_ed[1] = ip_ed[1].drop(columns='time') # We only need one 'time' column

# Combine the interpolated values in one DataFrame
synced = pd.concat(ip_ed, axis=1)    
out_file = 'synchronized.txt'
synced.to_csv(out_file)
print(f'Synchronized data saved to {out_file}' \
     + f', with a sample rate of {rate_sync} Hz.')