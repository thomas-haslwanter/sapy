""" Show how events can be elegantly detected using binary indexing """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from scipy import signal, io
from pprint import pprint

# Get eye positions, sampled with 100 Hz
data_dir = r'..\..\data'
file_name = 'HorPos.mat'
in_file = os.path.join(data_dir, file_name)

rate = 100
data = io.loadmat(in_file)
hor_pos = data['HorPos'][:,0]

# General layout of the plot
fig, axs = plt.subplots(3,2)
mpl.rc('lines', lw=0.8)         # Set the default line-width to '0.8'

# Select an interesting domain
my_domain = range(9000, 13500)
axs[0,0].plot(hor_pos[my_domain])
axs[0,0].set_ylabel('Position')
axs[0,0].tick_params(labelbottom=False) # equiv. to axs[0,0].set_xticklabels([])
axs[0,0].margins(x=0)

# Plot the absolute eye velocity
eye_vel = signal.savgol_filter(hor_pos, window_length=71, polyorder=3,
        deriv=1, delta=1/rate)
eye_vel_abs = np.abs(eye_vel)
axs[1,0].plot(eye_vel_abs[my_domain])

# Set a default threshold, in case the threshold is not determined interactively
threshold = 6.3
axs[1,0].axhline(threshold, color='C1')
axs[1,0].tick_params(labelbottom=False)
axs[1,0].margins(x=0)
axs[1,0].set_ylabel('Velocity')

# To find the threshold interactively, use the following lines
# I like to put the user-instructions in the window-title:
#plt.gcf().canvas.set_window_title('Select the threshold')
#selectedPoint = plt.ginput(1);       # ginput returns a list of (x/y)-tuples
#threshold = selectedPoint[0][1];     # I only want the y-value
#plt.gcf().canvas.set_window_title('')

# Plot3: show where the absolute velocity exceeds the threshold
is_fast = eye_vel_abs > threshold
axs[2,0].plot(is_fast[my_domain], 'o-', ms=2)   # 'ms' is short for 'markersize'
axs[2,0].set_ylabel('Above threshold')
axs[2,0].margins(x=0)

# Plot4: as Plot3, but zoomed in
close_domain = range(9900, 10600, 1)
axs[0,1].plot(is_fast[close_domain], 'o-', ms=2)
axs[0,1].set_ylabel('Above threshold')
axs[0,1].tick_params(labelbottom=False)
axs[0,1].margins(x=0)

# Plot5: Find the start and end of each movement
start_stop = np.diff(is_fast*1)   # "*1": to convert boolean signal to numerical
axs[1,1].plot(start_stop[close_domain])
axs[1,1].set_ylabel('Start / Stop')
axs[1,1].margins(x=0)

axs[2,1].axis('off')        # removes the empty axis to the lower right
plt.tight_layout()

# Save and show the figure
out_file = 'event_detection.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()

# Find the start and end times for all movements (in sec)
movement = {}
movement['StartTimes'] = np.where(start_stop ==  1)[0]/rate
movement['EndTimes']   = np.where(start_stop == -1)[0]/rate
pprint(movement)        # 'pprint' gives a nicer printout than 'print'

