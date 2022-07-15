""" Solution Exercise 'Gait Analysis', Chapter 'Statistics' """

# author:   Thomas Haslwanter
# date:     July-2022

# Import the required packages
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import io
import seaborn as sns

# Set the parameters
in_dir = '../../data'
file_name = 'gait.mat'

# Get the data
in_file = os.path.join(in_dir, file_name)
data = io.loadmat(in_file)

# Extract them from the Matlab format
time = data['Gaitdata']['time'][0][0].ravel()
gait = data['Gaitdata']['kneeAngle'][0][0].ravel()
heel_strike = data['Gaitdata']['heelStrike'][0][0].ravel()

# Show the original data
plt.plot(time, gait)
plt.xlabel('Time (s)')
plt.ylabel('Knee-Angle')
plt.show()

# Convert the heel-strike information from time (s) to an integer index
sample_rate = 1/(time[1] - time[0])
heel_strike_idx = np.int32(np.round(heel_strike * sample_rate))

# Make one interpolated cycle exatly 101 long, so that we can interpret it
# as percent (from 0 to 100). Note that the last point is included, since
# the heel-strikes also include the first AND last point
n_interp = 101

steps = []
for ii, step_length in enumerate(np.diff(heel_strike_idx)):
    steps.append(np.interp(np.arange(n_interp),
                 np.linspace(0, n_interp, step_length+1),
                 gait[heel_strike_idx[ii]:(heel_strike_idx[ii+1]+1)]))

# Convert from list to array, and calculate mean and std
data = np.array(steps)
mean = np.mean(data, axis=0)
std = np.std(data, axis=0, ddof=1)

# Show the result
sns.set_theme('notebook')
sns.set_style('ticks')
plt.plot(mean, label='mean')
plt.plot(mean + 2*std, ls='dashed', label='95%-CI')
plt.plot(mean - 2*std, ls='dashed', color='C1')
plt.legend()
plt.xlabel('Gait-cycle (%)')
plt.ylabel('Knee-angle (deg)')
plt.gca().margins(x=0)
out_file = 'gait.jpg'
pil_kwargs = {'quality': 90}
plt.savefig(out_file, dpi=200, pil_kwargs=pil_kwargs)
print(f'Result saved to {out_file}')
plt.show()

# the same plot, but with a shaded patch for the CIs
plt.plot(mean, label='mean')
#plt.plot(mean + 2*std, ls='dashed', label='95%-CI')
#plt.plot(mean - 2*std, ls='dashed', color='C1')
plt.fill_between(np.arange(len(mean)), mean-2*std, mean+2*std,
                 alpha=0.2, label='95%-CI')
plt.legend()
plt.xlabel('Gait-cycle (%)')
plt.ylabel('Knee-angle (deg)')
plt.gca().margins(x=0)
out_file = 'gait.jpg'
# plt.savefig(out_file, dpi=200, pil_kwargs=pil_kwargs)
# print(f'Result saved to {out_file}')
plt.show()
