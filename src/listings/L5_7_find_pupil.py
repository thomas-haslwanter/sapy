""" Find the pupil-edge in an image of the eye, using sckit-image """

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
    show_me(data)
    
    # Calculate and show the histogram
    histo = np.histogram(data, bins=np.arange(0,256))
    plt.plot(histo[1][:-1], histo[0])
    plt.show()
    
    # Convert to black-and-white
    # for convenience, I choose the threshold automatically
    bw = data>80
    show_me(bw)
    
    # Fill the holes
    filled = np.invert(ndimage.binary_fill_holes(np.invert(bw)))
    show_me(filled)
    
    se = morphology.disk(10)
    closed = morphology.closing(filled, se)
    show_me(closed)
    
    edges = filters.sobel(closed)
    show_me(edges)
    
