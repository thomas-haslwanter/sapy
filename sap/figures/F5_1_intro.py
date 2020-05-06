""" Images for the intro-fig of Chapter 5 """

# author:   Thomas Haslwanter
# date:     May-2020

import numpy as np
import matplotlib.pyplot as plt

from skimage import color, feature

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'code_quantlets', 'utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')
    
#print(f'__file__={__file__:<35}')
#print(f' __name__={__name__:<20} ')
#print(f'__package__={str(__package__):<20}')

#from ..code_quantlets.utilities.SAP_mystyle import set_fonts, show_data 

# Formatting
set_fonts(14)

# Noisy sine
t = np.arange(0, 20, 0.05)
x = np.sin(t)
x_noisy = x + 0.06*t + 0.3*np.random.randn(len(x))

#plt.plot(t, x)
#show_data('sine.jpg')

fig, axs = plt.subplots(1,2)
axs[0].plot(t, x_noisy)
axs[1].plot(t, x)

show_data('noisy_sine.svg')

# BW-Image
img_file = r'..\..\Data\HagenbergRocks.jpg'
img = color.rgb2gray(plt.imread(img_file))

# Edges
edges = feature.canny(img, sigma=2.5)

fig, ax = plt.subplots(1,1)
#axs[0].imshow(img, cmap='gray')
#axs[0].axis('off')

ax.imshow(edges, cmap='gray')
ax.axis('off')

show_data('edges.png')