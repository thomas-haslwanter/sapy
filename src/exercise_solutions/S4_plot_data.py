""" Solution to Exercise 'Plotting Data', 'Data Display' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt


def plot_data(num_cycles:float=1, freq:float=1) -> None:
    """Calculate and plot a sine wave.
    
    Parameters
    ----------
    num_cycles: Number of cycles
    freq : Frequency of oscillation [Hz] 
           
    Examples
    --------
    plot_data(5, 0.3)
    """
               
    # Set the parameters
    amp = 1
    rate = 100       # [Hz]
    noise_amp = 0.5
    
    # Calculate the data
    dt = 1/rate
    omega = 2*np.pi*freq
    t_cycle = 1/freq
    
    t = np.arange(0, num_cycles*t_cycle, dt)
    x = amp * np.sin(omega*t) + noise_amp*np.random.randn(len(t))
    
    # Plot the data
    plt.plot(t, x);
    plt.xlabel('Time [s]');
    plt.ylabel('Signal');
    plt.title('Noisy Sine');
    
    plt.show()    
    

if __name__ == '__main__':
    plot_data(2, 0.3)
    
    
