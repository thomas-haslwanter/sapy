"""Solution Ex. 'Event Finding', Chapter 'Events' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

# Generate the data
in_dir = '../../data'
in_file = 'S6_1_data.npz'
full_in_file = os.path.join(in_dir, in_file)
data = np.load(full_in_file)

data_dict = dict(data)
sig = data_dict.pop('signal', None)  # Get the 'signal' key
features = data_dict                 # Assign the remaining dictionary to 'features'

# Find where the features occur in the signal
found_locations = dict()      # Empty dictionary
pattern_names = features.keys()

for pattern in pattern_names:
    # Calculate the cross correlation between signal and pattern
    r = signal.correlate(sig, features[pattern])
    lag = np.arange(len(r)) - len(features[pattern])
    
    # Find the maxima of that cross correlation, by ...
    # ... first finding the approximate matches ...
    threshold = 0.75 * np.max(r)
    approxLocations = (r > threshold)*1
    local_starts = np.where(np.diff(approxLocations) ==  1)[0]
    local_ends   = np.where(np.diff(approxLocations) == -1)[0]
    
    # ... and then the local maxima
    maxLocs = []
    for (start, end) in zip(local_starts, local_ends):
        locMax = r[start:end].argmax()
        # the "+1" is due to the fact that the "diff" (above) is one shorter than the input 
        maxLocs.append( lag[start+locMax] + 1)
    
    found_locations[pattern] = maxLocs
    
print('Found Locations:')
print(found_locations)

