""" Show the artifacts introduced by FIR-filters """

# author:   Thomas Haslwanter
# date:     June-2020

# Get the basic packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Generate the signal
t = np.linspace(0, 2*np.pi, 21)
data = np.cos(t)

b = np.ones(5)/5
filtered = signal.lfilter(b, 1, data)

plt.plot(t, data, '*-', label='cos')
plt.plot(t, filtered, 'o-', label='filtered', fillstyle='none')
plt.legend()

out_file = 'FFT_artifacts.jpg'
show_data(out_file)
