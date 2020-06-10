""" Normal distribution, with and without outlier """

# author:   Thomas Haslwanter
# date:     June-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Set the parameters
np.random.seed(1234)
mean_pop = 75
sd_pop = 12.5

# Generate the data
weights = np.random.randn(100) * sd_pop + mean_pop
outlier = 25

mean, sd = stats.norm.fit(weights)

x = np.linspace(-3*sd_pop, 3*sd_pop, 200) + mean_pop

# Plot the data
fig, axs = plt.subplots(1,2)
black = [0, 0, 0]

axs[0].hist(np.hstack((weights, outlier)), ec=black, lw=0.5)
axs[0].set_xlabel('Weight [kg]')
axs[0].set_ylabel('Frequency')
axs[0].set_title('With outlier')

axs[1].hist(weights, density=True, ec=black, lw=0.5)
axs[1].plot(x, stats.norm(mean, sd).pdf(x))
axs[1].set_xlabel('Weight [kg]')
axs[1].set_ylabel('Probability')
axs[1].set_title('Without outlier')

plt.tight_layout()

out_file = 'outliers.jpg'
show_data(out_file)