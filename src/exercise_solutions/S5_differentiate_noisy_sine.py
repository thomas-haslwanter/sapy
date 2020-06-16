"""Solution Ex. 'Differentiation of Noisy Data' of chapter 'Data Filtering' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Set the parameters
amp = 1
freq = 0.3
num_cycles = 5
rate = 100
noise_amp = 0.5

# Calculate the noisy sine-wave
dt = 1/rate
omega = 2*np.pi*freq
tCycle = 1/freq
t = np.arange(0, num_cycles*tCycle, dt) 
x = amp * np.sin(omega*t) + noise_amp*np.random.randn(len(t))


# Calculate and plot the first derivative of the noisy sine-wave
win_sizes = [31, 51, 101]
gray_levels = [0.85, 0.65, 0.2]

for (grayLevel, winSize) in zip(gray_levels, win_sizes):
    filtered = savgol_filter(x, winSize, 2, 1, dt)
    gray = grayLevel * np.ones(3)
    plt.plot(t, filtered, Color=gray)

plt.legend(( f'winSize: {win_sizes[0]}', 
       f'winSize: {win_sizes[1]}',
       f'winSize: {win_sizes[2]}'))
plt.show()
