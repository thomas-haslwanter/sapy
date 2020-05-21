""" Demonstration on how to numerically integrate a signal """

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from scipy.integrate import cumtrapz

# Generate velocity data
vel = np.hstack((np.arange(10)**2,
                  np.ones(4) * 9**2,
                  np.arange(9, 4, -1)**2,
                  np.ones(3) * 5**2,
                  np.arange(5, 0, -1)**2))
time = np.arange(len(vel))


## Plot the data
fig, axs = plt.subplots(3, 1, sharex=True)

axs[0].plot(time, vel, '*-')
axs[0].set_ylabel('Velocity [m/s]')


axs[1].plot(time, vel, '*-')
## Corresponding trapezoid corners
for ii in range(len(vel)-1):
    x = [time[ii], time[ii], time[ii+1], time[ii+1]]
    y = [0, vel[ii], vel[ii+1], 0]
    data = np.column_stack((x,y))
    axs[1].add_patch(patches.Polygon(data))
    axs[1].add_patch(patches.Polygon(data, fill=False))
    
axs[1].set_ylabel('Velocity [m/s]')
# p = patch(xverts,yverts,'b','LineWidth',1.5)

axs[2].plot(time, np.hstack([0, cumtrapz(vel)]))
axs[2].set_ylabel('Distance [m]')
axs[2].set_xlabel('Time [s]')
axs[2].set_xlim([0, len(vel)-1])

# Save and show the image
out_file = 'numericalIntegrationPy.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
