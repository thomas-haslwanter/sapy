""" Demonstration of basic morphological operations """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology
from os.path import abspath

# Generate the base image
data = np.zeros( (99,99) )
data[34:66, 33:67] = 1
data[85:87, 85:87] = 1
data[49:51, 49:51] = 0

# Show the original image
fig, ax = plt.subplots()
plt.gray()
ax.imshow(data)
ax.set_title('Original Image')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

out_file = r'../../Images/Square.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Original image saved to {abspath(out_file)}')

# Perform the morphological operations
selem = morphology.square(5)
fig, axs = plt.subplots(2,2, figsize=(8,8))


def show_modImage(image, function, ax, title):
    """ Perform a morphological operation on an image, and display it
        in the given axis """

    fcn = getattr(morphology, function)
    ax.imshow(fcn(image, selem=selem))
    ax.set_title(title)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


show_modImage(data, 'binary_erosion',  axs[0][0], 'Eroded')
show_modImage(data, 'binary_dilation', axs[0][1], 'Dilated')
show_modImage(data, 'binary_opening',  axs[1][0], 'Opended (Dilation after Erosion)')
show_modImage(data, 'binary_closing',  axs[1][1], 'Closed (Erosion after Dilation)')

out_file = r'../../Images/Square_Morphological.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Original image saved to {abspath(out_file)}')
plt.show()
