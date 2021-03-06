""" Demonstrate a fit to sinusoidal data """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the sine-wave
freq = 0.5
offset = 3
delta = np.deg2rad(45)
amplitude = 2
rate = 10
duration = 3 * np.pi
omega = 2 * np.pi * freq

# Time
dt = 1/rate
t = np.arange(0,duration, dt)

# Simulate a noisy sine-wave
np.random.seed(123)             # to make the noise reproducible
y = offset + amplitude * np.sin(omega*t + delta) + np.random.randn(len(t))

# Show the data
plt.plot(t, y, '--', label='noisy data')
plt.autoscale(axis='x', tight=True)

# Fit the data
M = np.column_stack( (np.ones(len(t)), np.sin(omega*t), np.cos(omega*t)) )
p = np.linalg.pinv(M)@y

# Extract the coefficients from the fit
found = {}
found['offset'] = p[0]
found['amp'] = np.sqrt(p[1]**2 + p[2]**2)
found['delta'] = np.rad2deg(np.arctan2(p[2], p[1]))
found['y'] = found['offset'] \
            + found['amp'] * np.sin(omega*t + np.deg2rad(found['delta']))

# Superpose the fit over the data
plt.plot(t, found['y'], label='fit', lw=3)

plt.legend(loc='lower right')
plt.axhline(ls='dotted')
plt.xlabel('Time [sec]')
plt.ylabel('Signal')

# Save and show the figure
out_file = 'sine_fit.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
