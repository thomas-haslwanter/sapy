""" Simulation of feed-forward and feedback systems 

To run this module, the Python-package 'control' must be installed """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control


def feedforward(tau: float) -> None:
    """Simulation of a feedforward system, using the Python package 'scipy.signal'
    'time', 'in_signal', 'num' and 'den' are taken from the global workspace
    
    Parameters
    ----------
    tau : time constant of a first order lag
    """

    # Define the transfer function
    my_system = signal.lti(num, den)
    
    # Simulate the feedforward response
    t_out, out_signal, x_out = signal.lsim(my_system, in_signal, time)
    
    # Show signals
    plt.plot(time, in_signal, label='Input')
    plt.plot(t_out, out_signal, '--', label='Output')
    
    # Format the plot
    plt.title(f"First order lag (tau={tau} sec)")
    plt.text(15, 0.8, "Simulated with 'scipy' ", fontsize=12)
    plt.xlabel('Time [sec]')
    plt.legend()
    plt.show()    
    
    
def feedback(tau: float, fb_gain: float) -> None:
    """Simulation of a negative feedback system, using the package 'control'.
    'time', 'in_signal', 'num' and 'den' are taken from the global workspace
    
    Parameters
    ----------
    tau : time constant of a first order lag [sec]
    fb_gain : feedback gain
    """
    
    # First, define the feedforward transfer function
    sys = control.TransferFunction(num, den)
    print(sys)          # 1 / (tau*s + 1)
    
    # Simulate the response of the feedforward system
    t_out, y_out, x_out = control.forced_response(sys, T=time, U=in_signal)
    
    # Then define a feedback-loop, with gain fb_gain
    sys_total = control.feedback(sys, fb_gain)
    print(sys_total)    # 1 / (tau*s + (1+k)) 
    
    # Simulate the response of the feedback system
    t_total, y_total, x_total = control.forced_response(sys_total,
                                                        T=time, U=in_signal)
    
    # Show the signals
    plt.plot(time, in_signal, '-', label='Input')
    plt.plot(t_out, y_out, '--', label='Feedforward')
    plt.plot(t_total, y_total, '-.', label='Feedback')
    
    # Format the plot
    plt.xlabel('Time [sec]')
    plt.title(f"First order lag (tau={tau} sec)")
    plt.text(15, 0.8, "Simulated with 'control' ", fontsize=12)
    plt.legend()
    
    
if __name__ == '__main__':
    # Run the two functions
    
    # Generate input signal for both functions, a step at t=1 [sec]
    time = np.arange(0, 25, 0.1)
    in_signal = np.zeros(time.size)
    in_signal[time>=1] = 1
    
    # For both simulations the feedforward system is a first order lag
    tau = 5
    num = [1]
    den = [tau, 1]
    
    fb_gain = 2     # For the feedback system
    
    feedforward(tau)
    feedback(tau, fb_gain)
    