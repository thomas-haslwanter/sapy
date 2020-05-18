""" Basic plotting commands, by showing position and velocity of two curves """

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Generate the data
t = np.arange(0,10,0.1)

x = np.sin(t)       # position
y = np.sin(2*t)     # velocity

vx = np.cos(t)
vy = 2*np.cos(2*t)

# Put the position in the top plot, and the velocity in the bottom
# Ensure that when you zoom into one, the other also gets adjusted
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

axs[0].plot(t, np.column_stack( (x,y) ))
axs[1].plot(t, np.column_stack( (vx, vy) ))

# Add the axis labels
axs[0].set_ylabel('Position [m]')
axs[1].set_xlabel('Time [sec]')
axs[1].set_ylabel('Velocity [m/s]')

# Set the x-limit (Note that since the x-axes are shared, we only have to do this once!)
axs[0].set_xlim([0, 10])

# Also put the date on the figure
fig.text(0.8, 0.02, date.isoformat(date.today()))

# If you want to change the properties of one of the lines, you can do that now
for ax in axs:
    lines = ax.get_lines()
    lines[0].set_linestyle('dashed')
    
# Add a legend
axs[0].legend(['x', 'y'])

# Save the figure
out_file = 'simple_figure.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()    
