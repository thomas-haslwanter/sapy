""" Linear and Cubic interpolations """

# Import the standard packages
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from scipy import signal

# Generate the data
x = np.arange(7)
y = np.sin(x)

# Linear interpolation
xi = np.arange(0, 6, 0.01)
yi = np.interp(xi, x, y)

# Cubic interpolation
cs = CubicSpline(x, y)
yic = cs(xi)

# Plot polynomial interpolations
plt.plot(x, y, 'ro', label = 'original data')
plt.plot(xi, yi, label='linear interpolation')
plt.plot(xi, yic, label='cubic spline')

# Format the plot
ax = plt.gca()
ax.set_yticks(np.linspace(-1, 1, 5))
ax.axhline(0, LineStyle='--')
plt.legend()

# Save and show the figure
out_file = 'interpolations.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
