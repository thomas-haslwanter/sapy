""" Generate and plot a STFT (Short Time Fourier Transformation) """

# author:   Thomas Haslwanter
# date:	    April-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

# Get the data
from scipy.io import wavfile
data_dir = r'..\..\Data'
file_name = 'vowels.wav'
in_file = os.path.join(data_dir, in_file)

# Make the stft
fs, data = wavfile.read(in_file)
plt.specgram(data, NFFT=512, Fs=fs, noverlap=256, cmap=cm.jet)

# Format and save the result
plt.xlabel('Time [sec]')
plt.ylabel('Frequency [Hz]')
plt.ylim([0, 8000])

out_file = 'stft.jpg'
show_data(out_file)
