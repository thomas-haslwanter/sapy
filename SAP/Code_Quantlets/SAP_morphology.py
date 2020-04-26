""" Demonstration of basic morphological operations """

# author:   Thomas Haslwanter
# date:     April-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')
    
    
def show_modImage(image, function, ax, title):
    """ Perform a morphological operation on an image, and display it
        in the given axis """
    
    fcn = getattr(morphology, function)
    ax.imshow(fcn(image, selem=selem))
    ax.set_title(title)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


if __name__=='__main__':
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

    out_file = 'Square.jpg'
    show_data(out_file)

    # Perform the morphological operations
    selem = morphology.square(5)
    fig, axs = plt.subplots(2,2, figsize=(8,8))

    show_modImage(data, 'binary_erosion',  axs[0][0], 'Eroded')
    show_modImage(data, 'binary_dilation', axs[0][1], 'Dilated')
    show_modImage(data, 'binary_opening',  axs[1][0], 'Opended (Dilation after Erosion)')
    show_modImage(data, 'binary_closing',  axs[1][1], 'Closed (Erosion after Dilation)')

    out_file = 'Square_Morphological.jpg'
    show_data(out_file)
