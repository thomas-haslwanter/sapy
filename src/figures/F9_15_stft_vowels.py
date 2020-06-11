""" Generate and plot a STFT (Short Time Fourier Transformation) """

# author:   Thomas Haslwanter
# date:	    June-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 

# Get the data
from scipy.io import wavfile
data_dir = r'..\..\Data'
file_name = 'vowels.wav'
in_file = os.path.join(data_dir, file_name)

# Make the stft
fs, data = wavfile.read(in_file)
plt.specgram(data, NFFT=512, Fs=fs, noverlap=256, cmap=cm.jet)

# Format and save the result
plt.xlabel('Time [sec]')
plt.ylabel('Frequency [Hz]')
plt.ylim([0, 8000])

out_file = 'stft.jpg'
show_data(out_file)
