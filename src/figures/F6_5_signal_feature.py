"""Generate an auto-correlation."""

# author:   Thomas Haslwanter
# date:     April-2021

import numpy as np
import matplotlib.pyplot as plt

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

if __name__ =='__main__':

    # Generate the data
    signal = np.zeros(20)
    signal[7:10] = 1
    signal[14:17] = 1

    feature = np.zeros(7)
    feature[2:5] = 1

    # Plot the auto-correlation
    set_fonts(14)
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(signal, 'o-')
    axs[0].hlines(0, -0.5, 20, ls='dotted')
    axs[0].set_xticks(np.arange(0, 21, 2))
    axs[0].set_xlim(-0.5, 20)
    axs[0].set_ylabel('Signal')
    axs[0].set_yticks([0, 0.5, 1])

    axs[1].plot(feature, 'o-')
    axs[1].hlines(0, -0.5, 20, ls='dotted')
    axs[1].set_xticks(np.arange(0, 20, 2))
    axs[1].set_xticks(np.arange(0, 21, 2))
    axs[1].set_xlim(-0.5, 20)
    axs[1].set_xlabel('Shift')
    axs[1].set_ylabel('Feature')
    axs[1].set_yticks([0, 0.5, 1])
    sig_file = 'CorrDemo.jpg'
    show_data(sig_file, out_dir='.')




