""" Images for the intro-fig of Chapter 5 """

# author:   Thomas Haslwanter
# date:     June-2020

import numpy as np
import matplotlib.pyplot as plt

from skimage import color, feature

# Import formatting commands 
from my_style import set_fonts, show_data 
    
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
