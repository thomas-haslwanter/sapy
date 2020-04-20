import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Get the data
from scipy.io import wavfile
in_file = r'..\..\..\Data\vowels.wav'

# Make the stft
fs, data = wavfile.read(in_file)
plt.specgram(data, NFFT=512, Fs=fs, noverlap=256, cmap=cm.jet)

# Format and save the result
plt.xlabel('Time [sec]')
plt.ylabel('Frequency [Hz]')
plt.ylim([0, 8000])

out_file = 'stft.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
