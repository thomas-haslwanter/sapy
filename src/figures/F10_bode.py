""" Produce a bode plot, label it, and save it to an outfile """

# author:   Thomas Haslwanter
# date:     June-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 


def bode_log(out_file):
    """Logarithmic presentation of transfer function """
    
    fig, axs = plt.subplots(2,1, sharex=True)
    
    # Bode magnitude plot
    axs[0].semilogx(w, mag) 
    axs[0].plot(w[index], mag[index], 'ro') # Indicate cut-off frequency
    
    # Bode phase plot
    axs[1].semilogx(w, phase)  
    axs[1].plot(w[index], phase[index], 'ro')
    
    # Format the plots
    axs[0].set_ylabel('Gain [dB]')
    axs[0].grid(True, ls='dotted')
    axs[0].margins(x=0)
    axs[0].annotate(r'$\omega = \frac{1}{\tau}$',
                xy=(w[index], mag[index]), xycoords='data',
                xytext=(-10, -50), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    
    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel('Phase [deg]')
    axs[1].set_yticks([0,-45,-90], minor=False)
    axs[1].margins(x=0)
    axs[1].grid(True, ls='dotted')
    axs[1].annotate(r'$\omega = \frac{1}{\tau}$',
                xy=(w[index], phase[index]), xycoords='data',
                xytext=(-10, 30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    show_data(out_file)

    
def bode_linear(out_file):
    """Linear presentation of transfer function """
    fig, axs = plt.subplots(2,1, sharex=True)

    # Bode magnitude plot
    axs[0].plot(w, 10**(mag/20))    
    axs[0].plot(w[index], 10**(mag[index]/20), 'ro')
    
    # Bode phase plot
    axs[1].plot(w, phase)  
    axs[1].plot(w[index], phase[index], 'ro')
    
    # Format the plots
    axs[0].set_ylabel('Gain [linear]')
    axs[0].set_ylim([-0.10,1.1])
    axs[0].margins(x=0)
    axs[0].grid(True, ls='dotted')
    axs[0].annotate(r'$\omega = \frac{1}{\tau}$',
                xy=(w[index], 10**(mag[index]/20)), xycoords='data',
                xytext=(10, 20), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    axs[1].set_xlabel('Frequency [Hz]')
    axs[1].set_ylabel('Phase [deg]')
    axs[1].margins(x=0)
    axs[1].set_yticks([0,-45,-90], minor=False)
    axs[1].grid(True, ls='dotted')
    axs[1].annotate(r'$\omega = \frac{1}{\tau}$',
                xy=(w[index], phase[index]), xycoords='data',
                xytext=(10, 30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    show_data(out_file)


if __name__ == '__main__':
    
    # Calculate the transfer function
    tau = 5
    sys = signal.lti([1], [tau, 1])
    w, mag, phase = signal.bode(sys)
    
    # Where to plot the marker
    index = np.argmin(np.abs(w-1/tau))
    
    set_fonts(14)
    
    bode_log('bode_log.jpg')
    bode_linear('bode_linear.jpg')
