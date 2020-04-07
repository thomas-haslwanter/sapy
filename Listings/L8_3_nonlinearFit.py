""" Demonstration of a non-linear fit """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def find_start(t, x):
    """ Find where the exponential decay approximately starts """

    max_val = np.max(x)
    level = 0.6
    threshold = max_val * level
    first_below = np.min(np.where(x<threshold)[0])
    return t[first_below]

# For the fit, define an error-function ...
def model(x, t):
    """ Returns the residuals of the expected function """
    return x[0] + x[1] * np.exp(-t/x[2])


def err_fun(x, t, y):
    """ Returns the residuals of the expected function """
    return model(x,t) - y

if __name__ == '__main__':

    # Define the parameters
    offset, amp, tau = 3, 4, 5
    t0, noise_amp = 10, 0.5

    # Generate the delayed noisy exponential decay
    time = np.arange(0, 30, 0.01)
    values = offset + amp*np.exp(-(time-t0)/tau) 
    values[time<t0] = offset + amp
    np.random.seed(123)
    values += noise_amp * np.random.randn(len(time))

    # Fit the model
    t_start = find_start(time, values)
    decay = time > t_start
    x0 = [0, 1, 1]  # initial values for the fit
    par = optimize.least_squares(err_fun, x0, args = (time[decay], values[decay]))
    print(f'Fitted parameters: {par.x}')

    plt.plot(time, values, '.', label='data')
    plt.plot(time[decay], model(par.x, time[decay]), label='fit')
    plt.legend()
    plt.xlabel('Time [s]')
    plt.show()
