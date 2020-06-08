""" Show the principle of windowing for FFTs """

# author:   Thomas Haslwanter
# date:     June-2020

# Get the basic packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import signal
from scipy.io import wavfile

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

# Set the parameters
in_dir = r'..\..\data'
in_file = 'a1.wav'
out_file = 'windowing.jpg'
slice = range(7000, 20000)

win_length = 500
win_index = range(2000, 2000+win_length)


# Get the data
full_in_file = os.path.join(in_dir, in_file)
rate, sound = wavfile.read(full_in_file)
a1 = np.float32(sound[slice])
time = np.arange(len(a1))/rate

a1 /= np.max(a1)
max_sound = np.max(a1[win_index])

# Make the plots -----------------------------------
fig, axs = plt.subplots(2,2)
thin = 0.2

# Sound
axs[0,0].plot(time, a1, lw=thin)
axs[0,0].margins(x=0)
axs[0,0].set_ylabel('Sound')
axs[0,0].set_xticklabels('')

# Window
window = np.zeros_like(time)
window[win_index] = signal.windows.hann(win_length)
axs[1,0].plot(time, window, color='C1')
axs[1,0].set_xlabel('Time [s]')
axs[1,0].set_ylabel('Window')
axs[1,0].set_ylim(0,1)
for ax in [axs[0,0], axs[1,0]]:
    for index in [min(win_index), max(win_index)]:
        ax.axvline(time[index], lw=0.5, ls='dashed')

# Sound & window
axs[0,1].plot(time[win_index], a1[win_index], lw=thin)
axs[0,1].plot(time[win_index], window[win_index]*max_sound)
axs[0,1].set_xticklabels('')
axs[0,1].set_yticks([-0.5, 0, 0.5])
axs[0,1].axhline(0, ls='dashed')

# Windowed sound
axs[1,1].plot(time[win_index], window[win_index]*a1[win_index], lw=0.6)
axs[1,1].plot(time[win_index], window[win_index]*max_sound,
              ls='dashed')
axs[1,1].set_yticks([-0.5, 0, 0.5])
axs[1,1].set_xlabel('Time [s]')
axs[1,1].set_ylabel('Windowed Sound')
              
for ax in axs.ravel():
    ax.margins(x=0)
    
plt.tight_layout()
show_data(out_file)
