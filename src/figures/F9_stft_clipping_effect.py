""" Short Time Fourier Transform
Show the effect of clipping and windowing on a cosine wave.
"""
    
# author: Thomas Haslwanter
# date:   June-2020

import numpy as np
from numpy import fft
import matplotlib.pyplot as plt
from typing import Tuple, List
from scipy.signal import windows

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

def powerSpect(data: np.ndarray, rate: float) -> Tuple:
    """Powerspectrum, calculated via Fourier Transfrom

    Parameters
    ----------
    data : signal
    rate : sampling rate [Hz]

    Returns
    -------
    Pxx : one-sided power spectrum
    freq : corresponding frequencies [Hz]
    """
    
    n_data = len(data)
    fft_coeffs = fft.fft(data)
    
    Pxx = np.abs(fft_coeffs)**2 / n_data
    freq = fft.fftfreq(n_data, 1/rate)
    
    nyq = int(len(Pxx)/2)
    return (Pxx[:nyq], freq[:nyq])
    

def showData(data: np.ndarray, rate: float, legend: str, axs: List) -> None:
    """Show data in time domain, and corresponding powerspectrum

    Parameters
    ----------
    data : signal
    rate : sample rate [Hz]
    legend : type of signal
    axs : axes in which to plot the signal and the powerspectrum
    """
    
    t = np.arange(len(x)) / rate
        
    # fig, axs = plt.subplots(2,1)
    axs[0].plot(t,x, label=legend)
    # axs[0].set_title(legend)

    
    # Calculate the powerspectrum
    (Pxx, freq) = powerSpect(x, rate)
    
    axs[1].plot(freq, Pxx, '.-', lw=0.5)
    axs[1].set_xlim(1, 5000)
    

if __name__ == '__main__':
    
    # Set the parameters
    sample_rate = 100000
    dt = 1./sample_rate
    f = 1000
    tMax = 0.01
    out_file = 'STFT_clip.jpg'
    
    fig, axs = plt.subplots(3, 2, figsize=(8,5))

    # Data ...
    t = np.arange(0, tMax, dt)
    x = np.cos(2*np.pi*f*t)

    # ... clipped ...
    y = x
    y[:199] = 0
    y[400:1001] = 0

    # ... and windowed
    z = y;
    window = windows.hann(201)
    z[199:400] = z[199:400]*window

    # Plot the data
    showData(x, sample_rate, 'Cosine wave', axs[0])
    showData(y, sample_rate, 'Clipped', axs[1])
    showData(z, sample_rate, '   Clipped\n& Windowed', axs[2])

    # Format the plot
    axs[0,0].set_title('Signal')
    axs[0,1].set_title('Power')

    axs[1,0].legend()
    axs[2,0].legend()
    for ax in axs[0].tolist()+axs[1].tolist():
        ax.set_xticklabels('')
    
    axs[2,0].set_xlabel('Time [s]')
    axs[2,1].set_xlabel('Frequency [Hz]')
    
    show_data(out_file)
