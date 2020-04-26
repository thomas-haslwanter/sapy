"""Solution_Assignment_IIR  Solution to the Assignment "IIR-filtering",
   Exercise 1
   """

# author:   Thomas Haslwanter
# date:     April-2020


# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def applyLeakyIntegrator(alpha, x):
    """
    Parameters
    ----------
        alpha : float
            Decay rate of leaky integrator
        x : ndarry (N,)
            input data

    Return
    ------
    filtered : numpy vector (N,)
            Filtered data

    Example
    -------
    filtered = applyLeakyIntegrator(0.3, np.random.randn(200))
    """

    b = [alpha]
    a = [1, -(1-alpha)]
    filtered = signal.lfilter(b, a, x)

    return filtered


if __name__ == '__main__':
    # Prepare the input step, and the time-axis for plotting
    x = np.zeros(50)
    x[10:] = 1
    t = np.arange(len(x))

    # Plot the response, for different values of alpha
    alphas = [0.1, 0.2, 0.5, 0.9]
    colors = 'brgk'

    for (alpha, color) in zip(alphas, colors):
        plt.plot(t, applyLeakyIntegrator(alpha, x), Color=color)

    plt.xlabel('Time')
    plt.ylabel('Step-responses')
    plt.legend(alphas)

    plt.show()
