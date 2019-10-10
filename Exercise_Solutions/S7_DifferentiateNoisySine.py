"""Solution Exercise Chapter 5, "Derivative of noisy data"
"""

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Set the parameters
amp = 1
freq = 0.3
numCycles = 5
rate = 100
noiseAmp = 0.5

# Calculate the noisy sine-wave
dt = 1/rate
omega = 2*np.pi*freq
tCycle = 1/freq
t = np.arange(0, numCycles*tCycle, dt) 
x = amp * np.sin(omega*t) + noiseAmp*np.random.randn(len(t))


# Calculate and plot the first derivative of the noisy sine-wave
winSizes = [31, 51, 101]
grayLevels = [0.85, 0.65, 0.2]

for (grayLevel, winSize) in zip(grayLevels, winSizes):
    filtered = savgol_filter(x, winSize, 2, 1, dt)
    gray = grayLevel * np.ones(3)
    plt.plot(t, filtered, Color=gray)

plt.legend(( f'winSize: {winSizes[0]}', 
       f'winSize: {winSizes[1]}',
       f'winSize: {winSizes[2]}'))
plt.show()
