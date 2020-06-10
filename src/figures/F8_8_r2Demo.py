""" Demonstration of different correlation coefficients """

# author:   Thomas Haslwanter
# date:     June-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Set the parameters
x = np.arange(1000)
SDs = [10, 150, 1000]
np.random.seed(123)

# Generate and plot the data
fig, axs = plt.subplots(1,3, sharey=True)
for ii in range(3):
    y = x + np.random.randn(len(x))*SDs[ii]
    axs[ii].plot(x, y, '.')
    regression = stats.linregress(x,y)
    axs[ii].set_title(f'$r^2 = {regression.rvalue:5.3f}$')

axs[0].set_ylabel('Y')    
axs[1].set_xlabel('X')

out_file = 'regressionCoefficient.jpg'    
show_data(out_file)
