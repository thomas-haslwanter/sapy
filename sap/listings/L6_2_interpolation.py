""" Linear and Cubic interpolations """

# author:   Thomas Haslwanter
# date:     May-2020

# Import the standard packages
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from scipy import signal

from utilities.SAP_mystyle import set_fonts, show_data 

# Generate the data
x = np.arange(7)
y = np.sin(x)

# Linear interpolation
xi = np.arange(0, 6, 0.01)
yi = np.interp(xi, x, y)

# Cubic interpolation
cs = CubicSpline(x, y)
yic = cs(xi)

# Plot polynomial interpolations
set_fonts(14)
plt.plot(x, y, 'ro', label = 'original data')
plt.plot(xi, yi, label='linear interpolation')
plt.plot(xi, yic, label='cubic spline')

# Format the plot
ax = plt.gca()
ax.set_yticks(np.linspace(-1, 1, 5))
ax.axhline(0, LineStyle='--')
plt.legend()

out_file = 'interpolations.jpg'
show_data(out_file)
