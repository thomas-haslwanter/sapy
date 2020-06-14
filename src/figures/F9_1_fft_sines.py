""" Example of Fourier Transformation and Power-spectra

If you want the output to use the LaTeX-formatting, please
    i) make sure that LaTeX is installed properly on your system, and then
    ii) manually set the flag 'latex_installed' in line 22 to 'True'
"""
    

# author:   Thomas Haslwanter
# date:     June-2020

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
import os

# For simplified presentation
from utilities.my_style import set_fonts, show_data 

latex_installed = True
    
if latex_installed:
    import matplotlib
    matplotlib.rcParams['text.usetex'] = True

def generate_data() -> None:
    """ Generate sample data for the FFT-demo """

    # Generate some data, as a superposition of three sine waves
    # First set the parameters
    rate = 100      # [Hz]
    duration = 60   # [sec]
    freqs = [3, 7, 20]
    amps = [1, 2, 3]
    
    # Then calculate the data
    dt = 1/rate
    t = np.arange(0, duration, dt)
    
    # The clear way of doing it
    sig = np.zeros_like(t)
    for (amp, freq) in zip(amps, freqs):
        omega = 2 * np.pi * freq
        sig += amp * np.sin(omega*t)
        
    # Add some noise, and an offset
    np.random.seed(12345)
    offset = 1
    sig += np.random.randn(len(sig))*5 + offset
    
    # Note that the same could be achived with a single line of code.
    # However, in my opinion that is much less clear
    #sig = np.ravel(np.atleast_2d(amps) @ np.sin(2*np.pi * np.c_[freqs]*t)) + \
        #np.random.randn(len(t))*5
        
    return (t, dt, sig)


def power_spectrum(t: np.ndarray, dt: float, sig: np.ndarray) -> None:
    """ Demonstrate three different ways to calculate the power-spectrum
    
    Parameters
    ----------
    t : time [sec]
    dt : sample period [sec]
    sig : sample signal to be analyzed
    """
    
    set_fonts(16)
    
    fig, axs = plt.subplots(1,2, figsize=(10, 5))
    
    if latex_installed:
        txt ='$\displaystyle signal=offset + \sum_{i=0}^{2} a_i*sin(\omega_i*t)$'
        label = '$|FFT|^2$'
    else:
        txt = 'signal = offset + sum(i=0:2) a_i*sin(omega_i*t)'
        label = '|FFT|^2'
        
    # From a quick look we learn - nothing
    axs[0].plot(t, sig, '--')
    axs[0].set_xlim(0,1)
    axs[0].set_ylim(-15, 25)
    axs[0].set_xlabel('Time [s]')
    axs[0].set_ylabel('Signal')
    axs[0].text(0.5, 24, s=txt, fontsize=16)
    
    # Calculate the power spectrum by hand
    fft = np.fft.fft(sig)
    print(fft[:3])
    Pxx = np.abs(fft)**2
    
    # The easiest way to calculate the frequencies
    freq = np.fft.fftfreq(len(sig), dt)
    
    axs[1].plot(freq, Pxx, '--')
    axs[1].set_xlim(-50, 50)
    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel(label)
        
    axs[1].set_yticklabels([])
    plt.savefig('FFT_sines.svg')
    plt.show()
    #show_data('FFT_sines.jpg')
    
    # With real input, the power spectrum is symmetrical and we only one half
    Pxx = Pxx[:int(len(Pxx)/2)]
    freq = freq[:int(len(freq)/2)]
    
    # Showing the same data on a linear and a log scale
    fig, axs = plt.subplots(2,1, sharex=True)
    axs[0].plot(freq, Pxx, '--')
    axs[0].set_ylabel('Power')
    axs[1].semilogy(freq, Pxx, '--')
    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel('Power [dB]')
    show_data('FFT_sines_power_lin_log.jpg')
    
    # Periodogram and Welch-Periodogram
    f_pgram, P_pgram = signal.periodogram(sig, fs = 1/dt)
    f_welch, P_welch = signal.welch(sig, fs = 100, nperseg=2**8)
    
    fig, axs = plt.subplots(2, 1, sharex=True)
    
    axs[0].semilogy(f_pgram, P_pgram, '--', label='periodogram')
    axs[1].semilogy(f_welch, P_welch, '--', label='welch')
    
    axs[0].set_ylabel('Spectral Density [dB]')
    axs[0].legend()
    axs[0].set_ylim(1e-4, 1e3)
    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel('Spectral Density [dB]')
    axs[1].legend()
    show_data('FFT_sines_periodogram.jpg')
    

if __name__ == '__main__':
    data = generate_data()
    
    power_spectrum(*data)
    # Equivalent to: 
    # power_spectrum(data[0], data[1], data[2])
    
