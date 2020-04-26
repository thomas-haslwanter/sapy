"""Demonstration of the application of the Fourier Transformation to a repeating step function"""

# author:   Thomas Haslwanter
# date:     April-2020

import numpy as np
import matplotlib.pyplot as plt

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

# Generate and plot a stepping signal
t = np.arange(0, 2, 0.01)
x = np.round( np.mod(t, 1))

# Calculate the Fourier Transformation
X_fft = np.fft.fft(x)

# Show how the first few components contribute
fig, axs = plt.subplots(4, 1, sharex=True)
for ii, n in enumerate([1, 5, 13, 21]):
    if n == 1:
        axs[ii].plot(t, x, label='original')
    else:
        axs[ii].plot(t, x)
    fft_approx = np.copy(X_fft)
    fft_approx[n+2:-(n+1)] = 0
    approx = np.fft.ifft(fft_approx)
    axs[ii].plot(t, approx, label='n='+str(n))
    axs[ii].legend(loc='lower right')

# Save the result
out_file = 'FFT_demo.jpg'
show_data(out_file)
