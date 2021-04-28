"""Introduction Fourier Transformation: Application to Piano-sound 

This script produces Figs. 9.2, 9.9, 9.10, 9.12"""

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sksound
from scipy import signal

# For simplified presentation
from utilities.my_style import set_fonts, show_data 

    
def get_data(in_file, sound_time, time_slice):
    """Get the required data"""
    
    # Get the data
    sound = sksound.sounds.Sound(in_file)
    
    # Select the time when the tone is clear
    a1 = sound.data[sound_time]
    a1_range = a1.max() - a1.min()
    a1 = a1 / a1_range
    time = np.arange(len(a1))/sound.rate
    
    # Calculate the power-spectrum by hand
    a1_fft = np.fft.fft(a1)
    Pxx = np.abs(a1_fft)**2
    
    dt = 1/sound.rate
    duration = dt*len(a1)
    freq = np.arange(len(a1))/duration
    
    # Normalize to 'density'
    Pxx = Pxx *2/(np.sum(Pxx)/duration)
    
    return time, a1, sound.rate, freq, Pxx, duration
    

def fourier_intro(time, data, freq, Pxx, time_slice, out_file):
    """Time- and frequency presentation of sound.
    Corresponds to Fig. 9.1 in the book"""

    fig, axs = plt.subplots(1,3)
    axs[0].plot(time, data, lw=0.5)
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Sound-pressure ()')
    axs[0].margins(x=0)
    
    axs[1].plot(time, data)
    axs[1].set_xlim(time_slice)
    axs[1].set_xlabel('Time (s)')
    axs[1].set_yticklabels([])      
    
    axs[2].plot(freq, np.sqrt(Pxx))
    axs[2].set_xlim([0, 4000])
    axs[2].set_xlabel('Frequency (Hz)')
    axs[2].set_ylabel('|FFT| ()')
    axs[2].ticklabel_format(style='sci', scilimits=(0, 4))
    
    # Position the plots
    axs[0].set_position([0.125, 0.11, 0.2, 0.775])
    axs[1].set_position([0.35, 0.11, 0.2, 0.775])
    
    show_data(out_file)


def linear_and_log(freq, Pxx, out_file):
    """Comparison of linear and log representatino of powerspectrum
    Corresponds to Fig. 9.7 in the book.
    """

    fig, axs = plt.subplots(1,2)
    upper_limit = 4000
    axs[0].plot(freq, Pxx)
    axs[0].set_xlim([0, upper_limit])
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('Powerspectrum ()')
    axs[0].ticklabel_format(style='sci', scilimits=(0, 4))
    
    axs[1].semilogy(freq, Pxx, lw=0.5)
    axs[1].set_xlim([0, upper_limit])
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Powerspectrum (dB)')
    
    plt.tight_layout()
    
    show_data(out_file)


def noise_effects(time, sound, Pxx, time_slice, duration, out_file):
    """Effect of adding noise to a signal on the powerspectrum
    Corresponds to Fig. 9.8 in the book
    """

    # Note that a1 has been normalized to have a range of 1
    sound_noisy = sound + 1/100 * np.random.randn(len(sound))
    fft_noisy = np.fft.fft(sound_noisy)
    Pxx_noisy = np.abs(fft_noisy)**2
    
    # Normalize to 'density'
    Pxx_noisy = Pxx_noisy *2/(np.sum(Pxx_noisy)/duration)
    
    fig, axs = plt.subplots(1,2)
    axs[0].plot(time, sound, label='original')
    axs[0].plot(time, sound_noisy, label='noise added')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Sound-pressure ()')
    axs[0].set_xlim(time_slice)
    axs[0].legend()
    
    axs[1].semilogy(freq, Pxx, label='original', lw=0.5)
    axs[1].semilogy(freq, Pxx_noisy, label='noise added', lw=0.5)
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Powerspectrum (P**2/Hz)')
    axs[1].set_xlim([1200, 1700])
    
    plt.tight_layout()
    
    show_data(out_file)


def welch_periodogram(data, rate, freq, Pxx, out_file):
    """Comparison of simple powerspectrum to Welch-periodogram
    Corresponds to Fig. 9.9 in the book.
    """
    
    fig, axs = plt.subplots(1,2)
    f, welch = signal.welch(data, fs=rate,
                            nperseg=len(data)/8)
    df = np.diff(f)[0]
    # "normalize" welch
    welch = welch / (np.sum(welch)*df)
    
    axs[0].semilogy(freq, Pxx, label='Periodogram', lw=0.5)
    axs[0].semilogy(f, welch, label='Welch', lw=0.8)
    axs[0].set_xlim([0, rate/2])
    axs[0].set_ylabel('Powerspectrum (P**2/Hz)')
    axs[0].set_xlabel('Frequency (Hz)')
    
    axs[1].semilogy(freq, Pxx, label='Pxx')
    axs[1].semilogy(f, welch, label='Welch')
    axs[1].set_xlim([800, 1100])
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].legend()
    
    show_data(out_file)

if __name__ == '__main__':
    # Specify the parameters
    in_dir = '../../data'
    in_file = 'a1.wav'
    sound_time = range(7000, 20000)
    time_slice = [0.175, 0.185]
    out_files = ['FFT_intro.jpg', 'FFT_intro2.jpg', 'FFT_noise.jpg',
                 'FFT_periodogram.jpg']
    
    full_in_file = os.path.join(in_dir, in_file)
    
    (time, data, rate, freq, Pxx, duration) = get_data(full_in_file,
                                                       sound_time, time_slice)
    
    # Generate the four figures
    fourier_intro(time, data, freq, Pxx, time_slice, out_files[0])
    linear_and_log(freq, Pxx, out_files[1])
    noise_effects(time, data, Pxx, time_slice, duration, out_files[2])
    welch_periodogram(data, rate, freq, Pxx, out_files[3])
                
    print('Done!')
