""" Solution Exercise Chapter 7, 'Bandpass'
"""

# author:   Thomas Haslwanter
# date:     April-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Set the parameters
freqs = np.c_[[2, 30, 400]]
amps = np.r_[0.5, 1, 0.1]
rate = 5000
duration = 2

# Note that we want the "freq" as an numpy array, so we can normalize it afterwards
bandpass = {'freq': np.r_[10, 100],
            'order': 3}

# Calculate the signal
dt = 1/rate
t = np.arange(0, duration, dt)
t = np.atleast_2d(t)
nyq = rate/2   # Nyquist frequency
x = amps @ np.sin(2*np.pi * freqs @ t)   #If you don't believe it, do it explicitly

# Band-pass filter the data
[b,a] = signal.butter(bandpass['order'], bandpass['freq']/nyq, 'bandpass')
filtered = signal.lfilter(b,a,x)

# Show the data
fig, axs = plt.subplots(2,1, sharex=True)
# The "sharex" allows you to zoom in simultaneously on both axes

# The "flatten" turns a 2d-column array with one column into a plain vector
axs[0].plot(t.flatten(), x)
axs[0].set_ylabel('Rawdata')
axs[0].XTickLabels = []     # Only show the necessary information, no redundancy

axs[1].plot(t.flatten(), filtered)
axs[1].set_xlabel('Time [s]');
axs[1].set_ylabel('Filtered');

plt.show()
