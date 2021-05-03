""" Demonstration of the content of grayscale images """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import os

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Get the data
import skimage as ski
img = ski.data.camera()

# Make the plot
fig, axs = plt.subplots(1, 3, figsize=(10,4),
        gridspec_kw={'width_ratios':[1,1,0.1]})
plt.gray()

# Show the image
im_h = axs[0].imshow(img)

# Zoom in on the ear
axs[1].imshow(img)
axs[1].set_xlim([175, 195])
axs[1].set_ylim([145, 125])
axs[1].set_xticks(np.arange(175, 196, 5))
axs[1].set_yticks(np.arange(145, 124, -5))

# Show the colorbar, and position it such that it fits with the images
fig.colorbar(im_h, cax=axs[2])
plt.tight_layout()

box = axs[2].get_position()
pts = box.get_points()
pts[:,1] = [0.1, 0.95]
box.set_points(pts)
axs[2].set_position(box)

# Save and show the image
out_file = 'fit_regression.jpg'
show_data(out_file)
