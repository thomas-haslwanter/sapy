""" Demonstration of the content of grayscale images """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the data
import skimage as ski
img = ski.data.camera()

# Make the plot
fig, axs = plt.subplots(1, 3, figsize=(10,4), gridspec_kw={'width_ratios':[1,1,0.1]})
plt.gray()

# Show the image
im_h = axs[0].imshow(img)

# Zoom in on the ear
axs[1].imshow(img)
axs[1].set_xlim([210, 220])
axs[1].set_ylim([125, 115])

# Show the colorbar, and position it such that it fits with the images
fig.colorbar(im_h, cax=axs[2])
plt.tight_layout()

box = axs[2].get_position()
pts = box.get_points()
pts[:,1] = [0.1, 0.95]
box.set_points(pts)
axs[2].set_position(box)

# Save and show the image
out_file = r'..\Images\grayscale_demo.png'
plt.savefig(out_file, dpi=200)
print(f'Image saved to {os.path.abspath(out_file)}.')
plt.show()
