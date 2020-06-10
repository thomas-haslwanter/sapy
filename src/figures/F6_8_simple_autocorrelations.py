""" Show autocorrelations of two simple signals """

# author:   Thomas Haslwanter
# date:     June-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 


# Signal 1
x = np.zeros(20)
x[7:13] = 1
signals = [x]

# Signal 2
x = np.sin(np.arange(0, 12, 0.1))
signals.append(x)

# Make the plots
fig, axs = plt.subplots(2,2)
styles = ('.-', '-')

for  ii, sig in enumerate(signals):
    axs[ii, 0].plot(sig, styles[ii])
    axs[ii, 1].plot(np.correlate(sig, sig, mode='full'), styles[ii])
    for ax in axs[ii]:
        ax.axhline(0, ls='dotted')
        ax.margins(x=0)
        
axs[0,0].set_title('Signals')        
axs[0,1].set_title('Auto-Correlations')

out_file = 'simple_autocorrelations.jpg'
show_data(out_file)
