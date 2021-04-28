""" Solution Exercise 'EMG', Chapter 'Events' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import signal

# Set the parameters
in_dir = r'..\..\data'
file_name = 'Shimmer3_EMG_calibrated.csv'

# Get the data
in_file = os.path.join(in_dir, file_name)
df = pd.read_csv(in_file, skiprows=3, header=None, delim_whitespace=True)
df.columns = ['date', 'abs_time', 'cal', 'emg_1', 'emg_2']

# Either use a sample-rate of 512 Hz (from experimental protocol)
rate = 512

# or get the time from the time-stamps
df.abs_time = pd.to_datetime(df.abs_time)
df['time'] = df.abs_time - df.abs_time[0]
# convert from pandas format (nano-sec) into sec
df['t_sec'] = df.time.to_numpy(dtype=float)/1e9

# Show the original data
df.plot('t_sec', 'emg_1')
plt.ylabel('Signal (mV)')
plt.show()

# High-pass filter the data, to eliminate drifts
b, a = signal.butter(5, 1/(rate/2), 'high')
df['filtered'] = signal.lfilter(b, a, df.emg_1)

# Smooth the absolute value, to obtain the level of muscle activation
df['smoothed'] = signal.savgol_filter(np.abs(df.filtered), polyorder=3,
        window_length=101)

# Find onset and offset of muscle activations
threshold = 0.05
activity = df.smoothed > threshold

onset = np.where(np.diff(activity*1)==1)[0]
offset = np.where(np.diff(activity*1)==-1)[0]

# During the first ca. 4 sec we have startup-artifacts in the filtered data
# so we eliminate those events
onset = onset[onset>2000]
offset = offset[offset>2000]

# Make sure that we start with an onset ...
if onset[0] > offset[0]:
    offset = offset[1:]
# ... and end with an offset    
if offset[-1] < onset[-1]:
    onset = onset[:-1]
    
assert(len(onset)==len(offset))

# Eliminate short contractions, as they may be artifacts
min_interval = 0.5
onsets = []
offsets = []
for (start, stop) in zip(onset, offset):
    dt = (stop-start)/rate
    if dt > min_interval:
        onsets.append(start)
        offsets.append(stop)
        
# Convert onsets and offsets from lists to arrays
onsets = np.array(onsets)
offsets = np.array(offsets)

# Show the data
df.plot('t_sec', 'smoothed')
plt.plot(np.r_[onsets]/rate, np.zeros_like(onsets), 'ro')
plt.plot(np.r_[offsets]/rate, np.zeros_like(offsets), 'g*')
plt.show()

# And display the mean contraction time
print('The mean contraction time is' +
     f'{np.mean(offsets - onsets)/rate:5.2f} (sec)')
