"""Solution to Exercise 1 of the chaper 'Programming Background' """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

def rotate_me(in_vector, alpha):
    """Function that rotates a vector in 2 dimensions
    
    Parameters
    ----------
    in_vector : vector (2,) or array (:,2)
                vector(s) to be rotated
    alpha : float
            rotation angle [deg]
    
    Returns
    -------
    rotated_vector : vector (2,) or array (:,2)
                rotated vector
    
    Examples
    --------
    perpendicular = rotate_me([1,2], 90)
    
    """
    
    alpha_rad = np.deg2rad(alpha)
    R = np.array([[np.cos(alpha_rad), -np.sin(alpha_rad)],
    [np.sin(alpha_rad), np.cos(alpha_rad)]])
    return R @ in_vector


if __name__ == '__main__':
    
    vector = [2,1]
    # Draw a green line from [0,0] to [2,1]
    plt.plot([0,vector[0]], [0, vector[1]], 'g', label='original')
    
    # Coordinate system
    plt.hlines(0, -2, 2, linestyles='dashed')
    plt.vlines(0, -2, 2, linestyles='dashed')
    
    # Make sure that the x/y dimensions are equally drawn
    cur_axis = plt.gca()
    cur_axis.set_aspect('equal')
    
    # Rotate the vector
    rotated = rotate_me(vector, 25)
    plt.plot([0, rotated[0]], [0 ,rotated[1]], 
             label='rotated', 
             color='r', 
             linewidth=3)
             
    plt.legend()
    plt.show()