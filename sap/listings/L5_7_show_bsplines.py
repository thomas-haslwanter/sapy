"""Simple generation of B-splines"""

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01    # step interval for plotting
t = np.arange(0,1,dt)

# Generate the B-splines, through convolution
ones = np.ones(len(t))
Bsplines = [ones]
for ii in range(3):
    Bsplines.append(np.convolve(Bsplines[-1], ones))
    # Normalize the integral to "1"
    Bsplines[-1] /= np.sum(Bsplines[-1])*dt
    
# Plot the Bsplines    
set_fonts(16)
for spline in Bsplines:
    plt.plot(np.arange(len(spline))*dt, spline)

# Put on labels
plt.text(0.5, 1, '$b^0$', color='C0')
for ii in range(1,4):
    spline = Bsplines[ii]
    loc_max = np.argmax(spline)*dt
    val_max = np.max(spline)
    txt = '$b^' + str(ii) + '$'     # e.g. '$b^1$'
    color = 'C' + str(ii)           # e.g. 'C1'
    plt.text(loc_max, val_max, txt, color=color)

# Format the plot
plt.xlim(0, 4)
plt.xticks(np.arange(5))
plt.ylim(0, 1.1)

# Save and show the image
out_file = 'Bsplines.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
