"""Simple generation of B-splines"""

# author:   Thomas Haslwanterp
# date:     April-2020

import numpy as np
import matplotlib.pyplot as plt

dt = 0.01    # step interval for plotting
t = np.arange(0,1,dt)

# Generate the B-splines, through convolution
ones = np.ones(len(t))
Bsplines = [ones]
for ii in range(3):
    Bsplines.append(np.convolve(Bsplines[-1], ones))
    # Normalize the integral to "1"
    Bsplines[-1] /= np.sum(Bsplines[-1])*dt
    
# Plot the Bsplines    
for spline in Bsplines:
    plt.plot(np.arange(len(spline))*dt, spline)

plt.show()
