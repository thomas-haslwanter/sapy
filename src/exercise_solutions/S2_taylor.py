""" Solution to Exercise 'Taylor', Chapter 'Python' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def approximate(angle:np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Function that calculates a second order approximation to sine and cosine
    
    Parameters
    ----------
    angle : angle [deg]
    
    Returns
    -------
    approx_sine :  approximated sine 
    approx_cosine :  approximated cosine 
    
    Examples
    --------
    alpha = 0.1
    sin_ax, cos_ax = approximate(alpha)

    Notes
    -----
    Input can also be a single float
    
    """
    
    sin_approx = angle
    cos_approx = 1 - angle**2/2
    
    return (sin_approx, cos_approx)


if __name__ == '__main__':
    limit = 50          # [deg]
    step_size = 0.1     # [deg]    
    
    # Calculate the data
    theta_deg = np.arange(-limit, limit, step_size)    
    theta = np.deg2rad(theta_deg)
    sin_approx, cos_approx = approximate(theta)
    
    # Plot the data
    plt.plot(theta_deg, np.column_stack((np.sin(theta), np.cos(theta))), label='exact')    
    plt.plot(theta_deg, np.column_stack((sin_approx, cos_approx)), 
             linestyle='dashed', 
             label='approximated')             
    plt.legend()    
    plt.xlabel('Angle [deg]')    
    plt.title('sine and cosine')
    out_file = 'approximations.png'
    plt.savefig(out_file, dpi=200)
    print(f'Resulting image saved to {out_file}')
    
    plt.show()
