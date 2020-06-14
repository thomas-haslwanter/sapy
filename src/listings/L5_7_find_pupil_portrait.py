""" Find the pupil-edge in an image of the eye, using sckit-image

This version arranges all the output images into a single figure."""

# Import standard modules
import os
import numpy as np
import matplotlib.pyplot as plt

# Modules for image processing
from scipy import ndimage
from skimage import morphology 
from skimage import filters

def show_me(data):
    '''Show image data in graylevel'''
    plt.imshow(data, cmap='gray')
    plt.show()
    
if __name__ == '__main__':
    
    # Get the data ...
    data_dir = r'..\..\Data'
    file_name = 'eye.bmp'
    in_file = os.path.join(data_dir, file_name)
    data = plt.imread(in_file)
    
    # These settings ensure that the images and the histogram fit in nicely
    gs_kw = dict(hspace=0, wspace=0)
    fig, axs = plt.subplots(3, 2, constrained_layout=True, gridspec_kw=gs_kw)
    fig.set_size_inches([5, 6])
    
    # Show the original image
    plt.gray()
    pos = axs[0,0].imshow(data)
    
    # Calculate and show the histogram
    histo = np.histogram(data, bins=np.arange(0,256))
    axs[0,1].plot(histo[1][:-1], histo[0])
    
    # Since the histogram does not have the 4/3 aspect ration, I re-position it by hand
    axs[0,1].set_position([0.53, 0.68, 0.46, 0.29])
    
    # Convert to black-and-white
    # for convenience, I choose the threshold automatically
    bw = data>80
    axs[1,0].imshow(bw)
    
    # Fill the holes
    filled = np.invert(ndimage.binary_fill_holes(np.invert(bw)))
    axs[1,1].imshow(filled)
    
    # Eliminate the eye-brows and the bar on the left 
    se = morphology.disk(10)
    closed = morphology.closing(filled, se)
    axs[2,0].imshow(closed)
    
    # Find the edges
    edges = filters.sobel(closed)
    axs[2,1].imshow(edges)
    
    # To eliminates the axes, except for the histogram
    for ii, ax in enumerate(axs.ravel()):
        if ii == 1:
            ax.get_yaxis().set_visible(False)
        else:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
    
    out_file = 'eyes.jpg'
    plt.savefig(out_file, dpi=200)
    print(f'Image saved to {out_file}')
    
    plt.show()
    
