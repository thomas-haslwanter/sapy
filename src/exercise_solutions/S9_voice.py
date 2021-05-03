""" Solution Exercise 'Your voice', Chapter 'Spectral Analysis'

This example should be done with your own voice.
To show how to proceed, I use the sound in 'vowels.wav'.
"""

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import signal
import os
import sksound

# Set the parameters
in_dir = r'..\..\data'
file_name = 'vowels.wav'

# Get the data
in_file = os.path.join(in_dir, file_name)

# I perfer to work with "scikit-sound". But one can also read in the data
# directly with scipy.io
sound = sksound.sounds.Sound(in_file)

# Show the spectrogram
plt.specgram(sound.data, NFFT=512, Fs=sound.rate, noverlap=256, cmap=cm.jet)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power spectrum ()')
plt.show()

# Select a single vowel
o_sound = sound.data[265000:285000]

# Calculate the power-spectrum
f, Pxx = signal.periodogram(o_sound, fs=sound.rate)

# Show the result
plt.semilogy(f, Pxx)

# Format the plot
plt.ylim(1e-6, 1e2)
plt.xlim(0, 1000)
plt.title('ooooooooh')
plt.xlabel('Freq (Hz)')
plt.ylabel('Power spectrum ()')

plt.show()