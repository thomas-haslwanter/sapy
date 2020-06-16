""" Solution Exercises Chapter 'Spectral Analysis' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy import stats

# Exercise 1 =================================
 
# - The FFT has many frequency components, since the end of the sine-wave
#   does not match the beginning of the sine-wave.
# - In order to get an FFT with only one component, I have to type e.g.

# Generate the signal
duration = 2*np.pi
t = np.linspace(0, duration, 100)
x = np.sin(t)

# Calculate the power of the signal
x_fft = np.fft.fft(x)
Pxx = np.real(x_fft * np.conj(x_fft))

# Show the results
plt.plot(Pxx, '*-')
plt.show()

# - The first value is the offset.
# - The second and third values are the amplitude and phase of the first two
#   frequency components.
# - The frequency units are, the first value being the offset.
df = 1/duration


# Exercise 2  ---------------------------------------------
print('Solution Exercise 4 -------------------------');

# Enter the data
dt = 0.1
N = 100
t = np.arange(N)*dt
x = np.sin(t) + 3*np.cos(3*t)

# Calculate the DFT by hand
F = []
for ii in range(len(t)):
    F.append(0)
    for jj in range(len(t)):
        F[-1] += x[jj] * np.exp(-2*np.pi*1j*(ii)*(jj)/len(t))
F = np.array(F)
# Equivalent, elegant way to calculate the DFT:

n = np.arange(N)
k = np.arange(N)
n = np.atleast_2d(n)
k = np.atleast_2d(k)
dft = x @ np.exp(-2j*np.pi/N)**(n.T@k)

# And the calculation with the fft-function:
myFFT = np.fft.fft(x)

# Show the first three values

print('First 3 FFT components, calculated by hand (2 methods):');
print(F[:3])
print(dft[:3])

print('First 3 FFT components, calculated with the function "fft":');
print(myFFT[:3])
