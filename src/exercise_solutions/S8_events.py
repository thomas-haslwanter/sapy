"""Solution Chapter 8: Events """

# author:   Thomas Haslwanter
# date:     May-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from typing import Tuple


def X_Events() -> Tuple[np.ndarray, dict]:
    """ Generate a signal, containing steps and sine-waves

    Returns
    -------
    sig : ndarray(N,)
        Signal with steps and sine-waves
    templates : dictionary
        With fields 'step' and 'sine'

    Example
    -------
    sig, patterns = X_Events()
    """

    # Parameters
    rate = 100          # [Hz]
    noise_amp = 0.1
    signal_length = 50   # [sec]
    pattern_length = 50 # [pts]
    
    # At the following points there will be steps or sine-patterns
    locations = {'step':[500,  1500, 4400],
                 'sine':[1000, 2500, 4100] }
    num_pattern = len(locations['step'])

    print('True Locations:')
    print(locations)

    # Base signal
    dt = 1/rate
    t = np.arange(0, signal_length, dt)
    sig = np.random.randn(len(t)) * noise_amp

    # Step
    step = np.ones(pattern_length)
    step[:10] = 0
    step[40:] = 0

    # Sine
    sine_x = np.linspace(0, 2*np.pi, pattern_length)
    sine_y = np.sin(sine_x)

    # Put it all together
    for ii in range(num_pattern):
        onset = locations['step'][ii]
        sig[onset:onset+pattern_length] += step

        onset = locations['sine'][ii]
        sig[onset:onset+pattern_length] += sine_y

    # Templates
    templates = {'step':step, 'sine':sine_y}

    return (sig, templates)


if __name__ == '__main__':
    # Get the signal data and the templates
    sig, patterns = X_Events()
    
    # Find where the patterns occur in the signal
    found_locations = dict()      # Empty dictionary
    pattern_names = patterns.keys()
    
    for pattern in pattern_names:
        # Calculate the cross correlation between signal and pattern
        r = signal.correlate(sig, patterns[pattern])
        lag = np.arange(len(r)) - len(patterns[pattern])
        
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
    
