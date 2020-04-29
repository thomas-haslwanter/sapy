""" Show how events can be elegantly detected using binary indexing """

# author:   Thomas Haslwanter
# date:     April-2020

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, io
from pprint import pprint

# Get eye positions, sampled with 100 Hz
data_dir = r'..\..\Data'
file_name = 'HorPos.mat'
in_file = os.path.join(data_dir, file_name)

rate = 100
data = io.loadmat(in_file)
hor_pos = data['HorPos'][:,0]

# General layout of the plot
fig, axs = plt.subplots(3,2)

# Select an interesting domain
my_domain = range(9000, 13500, 1)
axs[0,0].plot(hor_pos[my_domain])
axs[0,0].set_ylabel('Eye Position [deg]')
axs[0,0].tickparams(labelbottom=False)

# Plot the absolute eye velocity
eye_vel = signal.savgol_filter(hor_pos, window_length=71, polyorder=3, deriv=1, delta=1/rate)
eye_vel_abs = np.abs(eye_vel)
axs[1,0].plot(eye_vel_abs[my_domain])

# Set a default threshold, in case the threshold is not determined interactively
threshold = 6.3
axs[1,0].axhline(threshold, color='r')
axs[1,0].tickparams(labelbottom=False)

#To find the threshold interactively, use the following lines
# set(gcf, 'Name', 'Select the threshold:')
# selectedPoint = ginput(1);
# threshold = selectedPoint(2); % I only want the y-value
# set(gcf, 'Name', '');

# Plot3: show where the absolute velocity exceeds the threshold
is_fast = eye_vel_abs > threshold
axs[2,0].plot(is_fast[my_domain], '*-')
axs[2,0].set_ylabel('Above threshold')
axs[0,1].tickparams(labelbottom=False)

# Plot4: as Plot3, but zoomed in
close_domain = range(9900, 10600, 1)
axs[0,1].plot(is_fast[close_domain], '*-')
axs[0,1].set_ylabel('Above threshold')

# Plot5: Find the start and end of each movement
start_stop = np.diff(is_fast*1)     # "*1": to convert boolean signal to numerical
axs[1,1].plot(start_stop[close_domain])
axs[1,1].set_ylabel('Start / Stop')

plt.show()

# Find the start and end times for all movements (in sec)
movement = {}
movement['StartTimes'] = np.where(start_stop ==  1)[0]/rate
movement['EndTimes']   = np.where(start_stop == -1)[0]/rate
pprint(movement)

