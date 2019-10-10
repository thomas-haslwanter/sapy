""" Show logical indexing """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt

# Create dummy data
time = np.arange(0,20,0.1)
data = np.sin(time)

# Set a threshold
threshold = 0.7

# Find the (binary) indices of all data above that threshold
isLarge = data > threshold

# Plot the data
fig, axs = plt.subplots(3,1)

axs[0].plot(time, data)
axs[1].plot(time[isLarge], data[isLarge])
axs[2].plot(data[isLarge])

# Format the plot
axs[0].set_ylabel('All data')

axs[1].set_ylabel('Large data')
axs[1].set_xlabel('Time [s]')

axs[2].set_ylabel('Large data only')
axs[2].set_xlabel('Points only')

plt.tight_layout()
plt.show()
