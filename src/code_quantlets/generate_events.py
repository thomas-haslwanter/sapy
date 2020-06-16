""" Generate data for Chapter 6: Exercise 1

Saves the data to 'S6_1_data.npz'
These data can be retrieved with the command
    new_data = np.load('S6_1_data.npz')
"""

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def generate_events() -> dict:
    """ Generate a signal, containing steps and sine-waves

    Returns
    -------
    data : dictionary
        With fields 
        - 'signal': numpy vector with 'signal' values
        - 'step'  : numpy vector with 'step' feature
        - 'sine'  : numpy vector with 'sine' feature

    Example
    -------
    data = X_Events()
    plt.plot(data['signal'])
    plt.show()
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
    data = {'signal':sig,
        'step':step,
        'sine':sine_y}

    return data


if __name__ == '__main__':
    # Get the signal data and the features
    data = generate_events()
    
    # Plot them
    fig, axs = plt.subplots(2,1)
    axs[0].plot(data['signal'], label='signal')
    axs[0].set_xlabel('Time [sec]')
    axs[0].legend()
    
    axs[1].plot(data['step'], label='step')
    axs[1].plot(data['sine'], label='sine')
    axs[1].set_xlabel('Time [sec]')
    axs[1].legend()
    
    plt.tight_layout()
    plt.show()
    
    # Save them to the file '
    out_file = 'S6_1_data'
    np.savez(out_file, **data)
    print(f'Data have been saved to {out_file}.npz')
    
    
