"""Figures for the chapter 'Statistics' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Use the "seaborn"-package for the figure styling
# (this is just a convenience wrapper for matplotlib settings)
sns.set(context='paper', style='ticks', font_scale=1.2)

# Generate the data
num_samples = 50
bmi = pd.DataFrame({'value':[27.3, 28.8, 26.5, 24.2]}, index=['Germany', 'USA', 'Austria','China'])
std = 4
samples = {}
np.random.seed(123)
for country in bmi.index:
    samples[country] = stats.norm(bmi.value[country], std).rvs(num_samples)

# Data and box-plot for Austria
fig, axs = plt.subplots(1, 2, sharey=True)

axs[0].plot(samples['China'], '.')
axs[0].set_xlabel('Subject-Nr')
axs[0].set_ylabel('$BMI \, [kg/m^2]$')
axs[0].set_title('Sample data from adult males - China')

axs[1].boxplot(samples['China'], sym='*')

out_file = 'BMI_data_China.svg'
show_data(out_file)

# Plot for the 1-sample T-test
plt.plot(samples['China'], 'o', label='China')
plt.hlines(25, 0, num_samples, linestyles='--')
plt.xlim(0, 50)
plt.xlabel('Subject-Nr')
plt.ylabel('BMI')
plt.legend()
out_file = 'BMI_China.jpg'
show_data(out_file)

# ... and do the corresponding T-test
t, p = stats.ttest_1samp(samples['China'], popmean=25)
print(f'Is China just at the limit of over-weight (BMI=25)? p={p}')

# Comparison between two independent groups
plt.plot(samples['Germany'], 'b*', ms=3, label='Germany')
plt.hlines(np.mean(samples['Germany']), 0, num_samples, linestyles='--', color='b',
        label='mean-Germany')

plt.plot(np.arange(num_samples, 2*num_samples), samples['Austria'],'ro', ms=3,
        fillstyle='none', label='Austria')
plt.hlines(np.mean(samples['Austria']), num_samples, 2*num_samples,
        linestyles='-.', color='r', label='mean-Austria')

plt.xlabel('Subject-Nr')
plt.ylabel('BMI')
plt.legend()
out_file = 'BMI_countries.jpg'
show_data(out_file)

# ... and again, the corresponding T-test
t, p = stats.ttest_ind(samples['Austria'], samples['Germany'])
print(f'Does Austria have the same BMI as the Germany? p={p}')

# For a paired T-test, simulate a slightly efficient diet
# (weight-loss 1 kg)
weight_loss = 1
samples['Germany2'] = samples['Germany'] - weight_loss + np.random.randn(num_samples)*0.5

fig, axs = plt.subplots(1,2, sharey=True)
axs[0].plot(samples['Germany'], 'o', ms=3, label='before diet')
axs[0].plot(np.arange(num_samples, 2*num_samples), samples['Germany2'],'o', fillstyle='none', ms=3, label='after diet')
axs[0].set_xlabel('Subject-Nr')
axs[0].set_ylabel('BMI')
axs[0].legend(loc='upper right')

axs[1].plot(samples['Germany'], 'o', ms=6, label='before diet')
axs[1].plot(samples['Germany2'],'o', ms=6, fillstyle='none', label='after diet')
axs[1].set_xlabel('Subject-Nr')
axs[1].set_xlim(-0.5, 5.5)
axs[1].legend(loc='upper right')

out_file = 'BMI_diet.jpg'
show_data(out_file)

# ... and again, the corresponding T-test
t, p = stats.ttest_rel(samples['Germany'], samples['Germany2'])
print(f'Was the diet in Germany effective? p={p}')
