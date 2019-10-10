""" Solution Exercise 7.9.1 'Integration as  IIR-filter'
"""

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the basic packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.signal import lfilter
from scipy import integrate
from collections import namedtuple

a = [1, -1]
b = {'quadratic':np.r_[-1, 20, 17]/36,
     'cumtrapz': np.r_[0.5, 0.5],
     'cumsum':  [1]}

Results = namedtuple('Results', ['calculated', 'filtered'])

# First show effect with 0:5
x = np.arange(6, dtype=float)

print('cumsum: -----------')
cumsum = Results(np.cumsum(x),
                 lfilter(b['cumsum'], a, x))
print(cumsum)

print('cumtrapz: -----------');
cumtrapz = Results(integrate.cumtrapz(x), 
                  lfilter(b['cumtrapz'], a, x) )
print(cumtrapz)

# For the quadratic fit, use a sine-wave
dt = 0.1    # [sec]
t = np.arange(0, 3*np.pi, dt)

# Calculate and show exact values of sine and its integral
si = np.sin(t)
co = np.cos(t)

plt.plot(t, si, label='sin')
plt.plot(t, 1-co, label='cos')

# Approximal integrals
integral = {}
integral['cumsum'] = np.cumsum(si) * dt
integral['cumtrapz'] = integrate.cumtrapz(si) * dt
integral['quadratic'] = lfilter(b['quadratic'], a, si) * dt

plt.plot(t, integral['cumsum'], '-*', label='cumsum')
plt.plot(t[1:], integral['cumtrapz'], '-o', label='cumtrapz')
plt.plot(t[:-1], integral['quadratic'][1:], 'k', label='quadratic fit');

plt.legend()
plt.show()

# Show the first ten numbers
print('cosine (exact) -----------')
print( 1-co[:10] )
print('sine integral: cumsum ------------')
print( integral['cumsum'][0:10:2] )
print('sine integral: cumtrapz ------------')
print( integral['cumtrapz'][0:10:2] )
print('sine integral: quadratic -------------')
print ( integral['quadratic'][2:12:2] )

