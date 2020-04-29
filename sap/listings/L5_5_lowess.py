""" Lowess and Loess-Smoothing """

# author:   Thomas Haslwanter
# date:     April-2020

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
from loess.loess_1d import loess_1d

# Generate some data
x = np.arange(0,10,0.1)
y = np.sin(x) + 0.2 * np.random.randn(len(x))

# Eliminate some, so that we don't have equal sampling distances
cur_ind = np.where( (x>5) & (x<6) )
x_space = np.delete(x, cur_ind)
y_space = np.delete(y, cur_ind)
plt.plot(x_space, y_space, '.', label='rawdata')

# Smooth the data with Lowess, from the package "statsmodels"
smoothed = lowess(y_space, x_space, frac=0.1)
index, data = smoothed.T
plt.plot(index, data, label='lowess')

# Smooth with Loess, from the package "loess"
x_out, y_out, weights = loess_1d(x_space, y_space, frac=0.1)
plt.plot(x_out, y_out, label='loess')
plt.legend()
plt.show()
