""" Show how to read in images, and mark selected locations """

import numpy as np
import matplotlib.pyplot as plt

# Set the filenames
in_file = r'..\..\Data\Saturn.jpg'
out_file = 'Saturn_marked.jpg'

# Get the data
img = plt.imread(in_file)

# Select the planets
plt.imshow(img)

fig = plt.gcf()
fig.canvas.set_window_title('Please select the moons:')

sel_pts = plt.ginput(4)
#sel_pts = np.array(selection, dtype='uint16')

# Mark the planets
ax = plt.gca()
for ii in range(len(sel_pts)):
    ax.add_artist(plt.Circle(sel_pts[ii],
        radius=30,
        color='g',
        lw = 4,
     fill=False))
    
# Show the result    
plt.pause(3)
    
# Save the resulting file
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
