""" Demonstration of the content of grayscale images """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the data
import skimage as ski
img = ski.data.camera()

# Make the plot
fig, axs = plt.subplots(1, 2)
plt.gray()

# Show the image
im_h = axs[0].imshow(img)

# Zoom in on the ear
axs[1].imshow(img>125)

# Save and show the image
out_file = 'bw_images.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
