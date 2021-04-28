""" Show principle of Savitzky-Golay filter """

# author:   Thomas Haslwanter
# date:     April-2021

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Set the parameters
p = [-4, 15, 4]
lower = 0.1
upper = 2.5
middle = (lower+upper)/2
dist = 1
np.random.seed(123)
set_fonts(8)

# Calculate the data
t = np.arange(-0.3, 3, 0.075)
data = np.array([np.polyval(p,x) + 1.5 * np.random.randn(1)[0] for x in t])

# Fit around the "middle"
index_fit = np.logical_and(lower<t, t<upper)
p_fit = np.polyfit(t[index_fit], data[index_fit], 2)
t_fit = np.arange(lower, upper, 0.02)

# Line-fit
bottom = middle-dist
top = middle + dist
t_fit2 = np.arange(bottom, top, 0.1)
slope = np.polyval(p_fit[:2]*[2,1], middle)
val_middle = np.polyval(p_fit, middle)

# make the plot
plt.hlines(0, -0.3, 3, ls='dashed', lw=2)
plt.vlines(0, -2, 24, ls='dashed', lw=2)

plt.plot(t, data, 'o', ms=6)
plt.plot(t_fit, np.polyval(p_fit, t_fit), lw=5)
plt.plot([lower, upper], 0.5 + val_middle+slope*(upper-lower)/2*np.r_[-1,1], lw=5)
plt.plot(middle, np.polyval(p_fit, middle), 'o', ms=15, c='C1')

# format plot
ax = plt.gca()
ax.set_xticklabels([])
ax.set_yticklabels([])

out_file = 'savgol_explained.png'
show_data(out_file)
