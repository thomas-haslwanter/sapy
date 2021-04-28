""" Shows how filters can be characterized. """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from typing import Tuple


def impulse_response(a, b, ax) -> None:
    """Show the impulse response of an IIR-filter.
    
    Parameters
    ----------
    a : array_like
        feedforward coefficients ('1' for FIR-filter)
    b : array_like
        feedback coefficients
    ax : mpl-axis
        plot-axis for the impulse response

    """

    # Define the impulse ...
    xImpulse = np.zeros(20)
    xImpulse[5] = 1

    # ... and find the impulse-response
    yImpulse = signal.lfilter(b, a, xImpulse)

    # Plot input and response
    ax.plot(xImpulse, '*-', label='Impulse')
    ax.plot(yImpulse, '*-', label='Response')
    ax.legend()
    ax.set_ylabel('Impulse Response')
    ax.set_xticks(np.arange(0, len(xImpulse), 5))
    ax.tick_params(axis='x', labelbottom=False)


def step_response(a, b, ax) -> None:
    """Show the impulse response of an IIR-filter.
    
    Parameters
    ----------
    a : array_like
        feedforward coefficients ('1' for FIR-filter)
    b : array_like
        feedback coefficients
    ax : mpl-axis
        plot-axis for the impulse response
    """

    # Define the step ...
    xStep = np.zeros(20)
    xStep[5:] = 1

    # ... and find the step-response
    yStep = signal.lfilter(b, a, xStep)

    # Plot step and response
    ax.plot(xStep, '*-', label='Step')
    ax.plot(yStep, '*-', label='Response')
    ax.legend(loc='lower right')
    ax.set_xticks( np.arange(0, len(xStep), 5) )
    ax.set_xlabel('n * T')
    ax.set_ylabel('Step Response')


def freq_response(a, b) -> Tuple[float, complex]:
    """ Show the impulse response of an IIR-filter. 
    
    Parameters
    ----------
    a : array_like
        feedforward coefficients ('1' for FIR-filter)
    b : array_like
        feedback coefficients

    Returns
    -------
    w : selected radial frequency of 
    h : complex gain for w
    """

    ## Frequency Response
    w, h = signal.freqz(b, a, fs=2)   # Calculate the normalized values
    # Plot them, in a new figure
    fig, axs = plt.subplots(2, 1, sharex=True)
    
    axs[0].plot(w, 20*np.log10( np.abs(h) ))
    axs[0].set_ylim([-40, 0])
    axs[0].set_ylabel('Magnitude [dB]')
    axs[0].set_title('Frequency Response')

    axs[1].plot(w, np.rad2deg(np.arctan2(h.imag, h.real)))
    axs[1].set_ylabel('Phase [deg]')
    axs[1].set_xlabel('Normalized Frequency (x pi rad/sample)')
    axs[1].set_xlim([0, 1])

    selFreq_val = 0.22 # Select a frequency point in the normalized response
    selFreq_nr = np.argmin( np.abs(w-selFreq_val) )
    selFreq_w = w[selFreq_nr]  # Value on plot

    # Find gain and phase for the selected frequency
    selFreq_h = h[selFreq_nr]
    gain = np.abs(selFreq_h)
    phase = np.rad2deg(np.angle(selFreq_h))

    # Show it on the plot
    dB = 20*np.log10(gain)
    axs[0].plot(selFreq_w, 20*np.log10( np.abs(selFreq_h) ), 'b*')
    axs[1].plot(selFreq_w,
                np.rad2deg(np.arctan2(selFreq_h.imag,selFreq_h.real)), 'b*')

    plt.show()

    return (selFreq_w, selFreq_h)
    

def show_filterEffect(w: float, h: complex) -> None:
    """ Demonstrate the filter effect on the selected frequency.

    Parameters
    ----------
    w : radial frequency
    h : complex gain
    """
    
    # Convert the normalized frequency to an absolute frequency
    rate = 1000
    
    nyq = rate/2
    dt = 1/rate
    freq = w * nyq    # Freqency in Hz, for the selected sample rate
    
    # Correct gain and phase
    gain = np.abs(h)
    phase = np.rad2deg(np.arctan2(h.imag, h.real))
    
    # Calculate the input and output sine, for 0.04 sec
    t = np.arange(0, 0.04, dt)
    sin_in = np.sin(2*np.pi * freq * t)
    sin_out = signal.lfilter(b, a, sin_in)
    
    # Plot them
    plt.plot(t, sin_in, label='Input')
    plt.plot(t, sin_out, label='Output')
    
    plt.title(f'Input and Response for {freq:4.1f} Hz, sampled at {rate}  Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Signal')
    
    # Estimate gain and phase-shift from the location of the second maximum
    # First find the two maxima (input and output)
    secondCycle = np.where( (t > 1/freq) & (t < (2/freq) ) )[0]
    
    secondMaxIn = np.max(sin_in[secondCycle])
    indexSecondMaxIn = np.argmax(sin_in[secondCycle])
    tMaxIn = t[secondCycle[indexSecondMaxIn]] 
    
    secondMaxFiltered = np.max(sin_out[secondCycle])
    indexSecondMaxFiltered = np.argmax(sin_out[secondCycle])
    tMaxOut = t[secondCycle[indexSecondMaxFiltered]] 
    
    # Estimate gain and phase-shift from them
    gain_est = secondMaxFiltered / secondMaxIn
    phase_est = (tMaxIn-tMaxOut)*360*freq
    
    # Plot them
    plt.plot(tMaxIn, secondMaxIn, 'b*')
    plt.plot(tMaxOut, secondMaxFiltered, 'r*')
    # legend('Input', 'Response', 'maxInput', 'maxResponse')
    plt.show()
    
    print(f'Correct gain and phase: {gain:4.2f}, and {phase:5.1f} deg')
    print(f'Numerical estimation: {gain_est:4.2f}, and {phase_est:5.1f} deg')
    
    # If you want to define the figure format, add the following:
    #fig = gcf
    #fig.PaperUnits = 'inches'
    #fig.PaperPosition = [0 0 6 3]
    

if __name__ == '__main__':

    ## Generate coefficients for an averaging filter (FIR)
    len_filter = 5
    b = np.ones(len_filter)/len_filter
    a = 1

    fig, axs = plt.subplots(2, 1, sharex=True)

    impulse_response(a, b, axs[0])
    step_response(a, b, axs[1])
    plt.show()

    w, h = freq_response(a, b)
    
    show_filterEffect(w, h)

