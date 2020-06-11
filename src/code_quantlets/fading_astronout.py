"""Add transparency layer to image."""

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required libraries
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

from utilities.my_style import set_fonts, show_data 

# Get a color-image
img = data.astronaut()
nrows, ncols = img.shape[:2]

# Make vectors from 1 to 0, with lengths matching the image
alpha_row = np.linspace(1, 0,ncols)
alpha_col = np.linspace(1, 0, nrows)

# Make coordinate-grids
X, Y = np.meshgrid(alpha_row, alpha_col)

# Scale the vector from 0 to 255, and 
# let the image fade from top-right to bottom-left
X_Y = np.uint8(X*Y * 255)
X_Y = np.atleast_3d(X_Y)  #make sure the dimensions matches the image

# Add the alpha-layer
img_alpha = np.concatenate( (img, X_Y), axis=2)

plt.imshow(img_alpha)

out_file = 'fading_astronout.png'
show_data(out_file)
