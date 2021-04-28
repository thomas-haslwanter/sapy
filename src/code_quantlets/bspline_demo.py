""" Demonstration of B-splines. """

# author:   stack-overflow user Fnord, comments by Thomas Haslwanter
# date:     April-2021

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si

from utilities.my_style import set_fonts, show_data 


def scipy_bspline(cv, n: int=100, degree: int=3, periodic: bool=False) -> np.ndarray:
    """ Calculate n samples on a bspline

    Parameters
    ----------
    cv :  Array of control vertices
    n  :  Number of samples to return
    degree :  Curve degree
    periodic : True - Curve is closed
    
    Returns
    -------
    spline_data : x/y-values of the spline-curve
    """

    cv = np.asarray(cv)
    count = cv.shape[0]

    # Closed curve
    if periodic:
        kv = np.arange(-degree,count+degree+1)
        factor, fraction = divmod(count+degree+1, count)
        cv = np.roll(np.concatenate((cv,) * factor + (cv[:fraction],)),-1,axis=0)
        degree = np.clip(degree,1,degree)

    # Opened curve
    else:
        degree = np.clip(degree,1,count-1)
        kv = np.clip(np.arange(count+degree+1)-degree,0,count-degree)

    # Return samples
    max_param = count - (degree * (1-periodic))
    spl = si.BSpline(kv, cv, degree)
    spline_data = spl(np.linspace(0,max_param,n))
    
    return spline_data


if __name__ == '__main__':
    
    cv = np.array([[ 50.,  25.],
       [ 59.,  12.],
       [ 50.,  10.],
       [ 57.,   2.],
       [ 40.,   4.],
       [ 40.,   14.]])
    

    set_fonts(12)
    plt.plot(cv[:,0],cv[:,1], 'o-', label='Control Points')

    ax = plt.gca()
    ax.set_prop_cycle(None)
    
    # for degree in range(1,7):
    for degree in [1, 2, 3]:
        p = scipy_bspline(cv, n=100, degree=degree, periodic=False)
        x,y = p.T
        plt.plot(x, y,  label='Degree %s'%degree)
    
    # Format the plot
    plt.legend()
    plt.xlim(35, 70)
    plt.ylim(0, 30)
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.set_aspect('equal', adjustable='box')

    # Show and save the output
    out_file = 'bsplines_example.jpg'
    show_data(out_file)
