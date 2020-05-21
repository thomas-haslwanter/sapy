""" Show logical indexing """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt

# Create a sine-wave
dt = 0.1
duration = 20
time = np.arange(0,duration,dt)
data = np.sin(time)

# Set a threshold
threshold = 0.7

# Find the (binary) indices of all data above that threshold
is_large = data > threshold

# For plotting of "large" data, set all "not large" data to "np.nan"
# Note that I explicitly copy the data!
large_data = data.copy()
large_data[~is_large] = np.nan

# Plot the data
fig, axs = plt.subplots(3,1)

axs[0].plot(time, data)
axs[0].plot(time, large_data, lw=3)
axs[1].plot(time[is_large], data[is_large], '*-')
axs[2].plot(data[is_large])

# Format the plot
axs[0].set_ylabel('All data')
axs[0].axhline(threshold, ls='dotted')
axs[0].margins(x=0)
axs[0].set_xticklabels([])

axs[1].set_ylabel('Large data')
axs[1].set_xlabel('Time [s]')
axs[1].margins(x=0)
axs[1].set_xlim(0, duration)
axs[1].set_ylim(-1.05, 1.05)

axs[2].set_ylabel('Large data only')
axs[2].set_xlabel('Points only')

# Group the top two axes, since they have the same x-scale
axs[0].set_position([0.125, 0.75, 0.775, 0.227])
axs[1].set_position([0.125, 0.50, 0.775, 0.227])
axs[2].set_position([0.125, 0.09, 0.775, 0.227])

# Save and show the figure
out_file = 'FindingEvents.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
