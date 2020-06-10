""" Demonstration on how to filter images """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import os

# For the image filtering
from scipy import ndimage

# Get the data
import skimage as ski
img = ski.data.camera()
img_f = np.array(img, dtype=float)   # for the filtering, the data must not be uint

# Make the filters
Filters = []
Filters.append(np.ones((11,11))/121)
Filters.append(np.array([np.ones(11),np.zeros(11),-1*np.ones(11)]))
Filters.append(Filters[-1].T)

# Filter the images
filtered = []
for filt in Filters:
    filtered.append( ndimage.correlate(img_f, filt) )

# Make the plots
fig, axs = plt.subplots(3,2, figsize=(6,8))
plt.gray()

axs[0,0].imshow(img)
axs[0,1].imshow(filtered[0])
axs[1,0].imshow(filtered[1])
axs[1,1].imshow(filtered[2])
axs[2,0].imshow(filtered[1]>125)
axs[2,1].imshow(filtered[2]>125)

# Remove the ticks and labels
for axis in axs.ravel():
    axis.axes.get_xaxis().set_visible(False)
    axis.axes.get_yaxis().set_visible(False)

# Reduce the space between the plots
plt.tight_layout()

# Save and show the figure
out_file = r'..\Images\filter_demo.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {os.path.abspath(out_file)}')
plt.show()
