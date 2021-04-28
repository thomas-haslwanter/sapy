""" Demonstration of the Nyquist criterium """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the basic packages
import numpy as np
import matplotlib.pyplot as plt

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Set the parameters
rate = 10
duration = 0.9 + 1e-5
freqs = np.atleast_2d([0.45, 2.2])  # row vector
out_file = 'Nyquist.jpg'


# Calculate the corresponding data
nyq = rate/2
dt = 1/rate
omega = 2 * np.pi * nyq * freqs

time = np.arange(0, duration, dt)
t_fast = np.arange(0, duration, dt/50) # Should be much higher

time = time[:, np.newaxis]          # column vector
t_fast = t_fast[:, np.newaxis]          

data = np.sin(time @ omega)
data_fast = np.sin(t_fast @ omega)


# Plot the data
fig, axs = plt.subplots(2,1)

for ii, ax in enumerate(axs):
    ax.plot(t_fast, data_fast[:, ii], lw=0.75, label='original')
    ax.plot(time, data[:, ii], '-o', label='recorded')
    ax.set_xticklabels('')
    ax.set_title(f'{freqs[0, ii]:4.2f} * f_nyquist')
    ax.margins(x=0)

axs[0].legend()

show_data(out_file)

