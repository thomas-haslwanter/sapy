"""Solution to Exercise 2 of the chaper 'Programming Background' """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

def approximate(angle):
    """Function that calculates a second order approximation to sine and cosine
    
    Parameters
    ----------
    theta : float or vector
            angle [deg]
    
    Returns
    -------
    approx_sine :  float or vector
                approximated sine 
    approx_cosine :  float or vector
                approximated cosine 
    
    Examples
    --------
    alpha = 0.1
    sin_ax, cos_ax = approximate(alpha)
    
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