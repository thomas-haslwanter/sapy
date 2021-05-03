""" Solution Exercise 'Power Spectrum', Chapter 'Spectral Analysis' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy import stats

# Generate the original data
t = np.arange(0, 10, 0.1)
x = np.sin(t)
fft = np.fft.fft(x)
amps = np.abs(fft)

# - The FFT has many frequency components, since the end of the sine-wave
#   does not match the beginning of the sine-wave. This is some form of
#   "spectral leakage"
# - In order to get an FFT with only one component, I have to type e.g.

# Generate the signal
duration = 2*np.pi
t = np.linspace(0, duration, 100)
x = np.sin(t)

# Calculate the power of the signal
fft_ideal = np.fft.fft(x)
amps_ideal = np.abs(fft_ideal)

# Show the results
plt.plot(amps_ideal**2, '*-')
plt.show()

# - The first value is real, since it is proportional to the offset.
# - The second and third values are the amplitude and phase of the first two
#   frequency components.
# - The frequency units are:
df = 1/duration

print('\nSolution Exercise 1 -------------------------');
print(f'The first three components are: {fft[:3]}')
print(f'The offset is: {amps[0]/len(x)}')
print('The first two oscillating components have the amplitudes: ' +
      f'{amps[1:3]}')
print('The phases of the first two components are: ' +
        f'{np.angle(fft[1:3])} (rad)')
print(f'The first two frequencies are: {[df, 2*df]} (Hz)')

