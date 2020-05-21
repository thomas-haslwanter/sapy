"""
This module offeres an example of a good Python documentation style.

"""

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def show_sine(amp=1,  freq=1, cycles=2, rate=100):
    """
    This function calculates and returns a noisy sine wave.
    The parameters offset, phase, and noise_amp are hardcoded.
    
    Parameters
    ----------
    amp : float
        Amplitude of the sine-wave
    freq : float
        Frequency of the sine-wave [Hz]
    cycles : float
        Number of oscillation cycles
    rate :  float
        Sample rate [Hz]

    Returns
    -------
    t : vector (N,) 
        Time base of the sine-wave [s]
    sine : vector (N,)    
        Noisy sine signal

    Example
    -------
    doc_demo.show_sine(amp=2, cyles=3)
    
    Notes
    -----

    .. math::
        signal = offset + amp * sin(\\omega*t + \\Delta) + noise\\_amp*\\mathcal{N}
    
    """
    
    # Set the parameters for a sine wave
    offset = 3
    delta = np.deg2rad(30)
    noise_amp = 0.5
    
    # Calculate the sine-values
    dt = 1/rate
    omega = 2*np.pi*freq
    
    t = np.arange(0, cycles/freq, dt)
    x = offset + amp * np.sin(omega*t + delta) + noise_amp * np.random.randn(len(t))
    
    plt.plot(t,x)    
    plt.xlabel('Time [sec]')    
    plt.ylabel('Signal')    
    
    plt.show()
    
    return (t, x)    

if __name__ == '__main__':
    t, val = show_sine(amp = 2, freq = 2, cycles=3)
