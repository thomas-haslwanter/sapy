""" Solution Ex. 'Integration as  IIR-filter' of Chapter 'Data Filtering' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the basic packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.signal import lfilter
from scipy import integrate
from collections import namedtuple

a = [1, -1]
b = {'cum_trapz': np.r_[0.5, 0.5],
     'cum_sum':  [1]}

Results = namedtuple('Results', ['calculated', 'filtered'])

# First show effect with 0:5
x = np.arange(6, dtype=float)

print('cum_sum: -----------')
cum_sum = Results(np.cumsum(x),
                 lfilter(b['cum_sum'], a, x))
print(cum_sum)

print('cum_trapz: -----------');
cum_trapz = Results(integrate.cumtrapz(x), 
                  lfilter(b['cum_trapz'], a, x) )
print(cum_trapz)

# For the quadratic fit, use a sine-wave
dt = 0.1    # [sec]
t = np.arange(0, 3*np.pi, dt)

# Calculate and show exact values of sine and its integral
si = np.sin(t)
co = np.cos(t)

plt.plot(t, si, label='sin')
plt.plot(t, 1-co, label='1-cos')

# Approximal integrals
integral = {}
integral['cum_sum'] = np.cumsum(si) * dt
integral['cum_trapz'] = integrate.cumtrapz(si) * dt

plt.plot(t, integral['cum_sum'], '-*', label='cum_sum')
plt.plot(t[1:], integral['cum_trapz'], '-o', label='cum_trapz')

plt.legend()
plt.show()

# Show the first ten numbers
print('cosine (exact) -----------')
print( 1-co[:10] )
print('sine integral: cum_sum ------------')
print( integral['cum_sum'][0:10:2] )
print('sine integral: cum_trapz ------------')
print( integral['cum_trapz'][0:10:2] )

