""" Fit a normal distribution """

# author:   Thomas Haslwanter
# date:     April-2021

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Set the parameters
np.random.seed(123)
mean_pop = 75
sd_pop = 12.5
n_data = 100

# Generate the data
weights = stats.norm(mean_pop, sd_pop).rvs(n_data)
weights += 5*np.random.randn(n_data)    # noise added

# Fit a normal curve to the data
mean, sd = stats.norm.fit(weights)
print(f'Original values:\tmean={mean_pop:4.1f}, sd={sd_pop:4.1f}')
print(f'Fit values:\t\t\tmean={mean:4.1f}, sd={sd:4.1f}')

x = np.linspace(-3*sd_pop, 3*sd_pop, 200) + mean_pop

# Plot the data
fig, axs = plt.subplots(1,2)
black = [0, 0, 0]

axs[0].hist(weights, ec=black, lw=0.5)
axs[0].set_xlabel('Weight [kg]')
axs[0].set_ylabel('Frequency')

axs[1].hist(weights, density=True, ec=black, lw=0.5, label='Data', alpha=0.4)
axs[1].plot(x, stats.norm(mean, sd).pdf(x), label='Fit')
axs[1].plot(x, stats.norm(mean_pop, sd_pop).pdf(x), ls='dashed', label='Original')
axs[1].set_xlabel('Weight [kg]')
axs[1].set_ylabel('Probability')
axs[1].legend()

plt.tight_layout()

out_file = 'normal_fit.jpg'
show_data(out_file, out_dir='.')