""" Demonstration of the princple behind B-splines """

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01    # step interval for plotting
t = np.arange(0,1,dt)

# Generate the B-splines, through convolution
ones = np.ones(len(t))
Bsplines = [ones]
for ii in range(1):
    Bsplines.append(np.convolve(Bsplines[-1], ones))
    # Normalize the integral to "1"
    Bsplines[-1] /= np.sum(Bsplines[-1])*dt
    
# Plot the Bsplines    
spline = Bsplines[1]
n_spline = len(spline)
t_base = np.arange(len(spline))*dt

knots = [[1, 2, 3],
         [2, 3, -0.5]]

num_pts = len(knots[0])
t_total = np.arange(0, 1+num_pts, dt)
x_total = np.zeros_like(t_total)

for ii in range(num_pts):
    plt.plot(ii + t_base, spline, ls='dashed')
    plt.plot(knots[0][ii], knots[1][ii], 'o', color='C'+str(ii),ms=10)
    x_total[ii*len(t):(ii+2)*len(t)-1] += spline*knots[1][ii]

plt.plot(t_total, x_total, 'k', lw=0.5)

# Format the plot
plt.xlim(0, 4)
plt.xticks(np.arange(5))
plt.axhline(0, color='k', lw=0.3)
plt.xlabel('x')
plt.ylabel('y')

# Save and show the image
out_file = 'Bsplines_1d.jpg'
plt.savefig(out_file, dpi=200, quality=90)
plt.grid(True, ls='dashed')
print(f'Image saved to {out_file}')

plt.show()
