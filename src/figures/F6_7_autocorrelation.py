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

    # Determine the auto-correlation 
    auto_corr = np.correlate(signal, signal, 'full')
    shift = np.arange(len(auto_corr)) - (len(signal)-1)

    # Plot the auto-correlation
    set_fonts(14)
    plt.plot(shift, auto_corr)
    plt.xlabel('Shift')
    plt.ylabel('Auto-Correlation')

    ax = plt.gca()
    ax.margins(x=0)

    # Show and save the result
    out_file = 'autoCorrelation.jpg'
    show_data(out_file)
