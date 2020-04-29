"""Simple program to demonstrate how to comment Python code

This program contains a sample function, as well as a test-section which allows
you to test the function. Note that the lines in a program should always be
shorter than 80 characters!                                               80 >>|

Module headers and function headers should use tripple quotes, single comment 
lines should use "#"
"""

# author:   Thomas Haslwanter
# date:     April-2020

# First import the required packages
import numpy as np


def add_me(x, y):
    """Adds to inputs of the same dimension
    
    Parameters
    ----------
    x : float or ndarray
        First input parameter
    y : float or ndarray
        Second input parameter. Has to have a shape matching "x"
    
    Returns
    -------
    sum : float or ndarray
        The sum of "x" and "y". The numpy "broadcasting"-rules determine the
        dimension of "sum".
        
    Example
    -------
    >>> x = np.arange(4, 10)
    >>> y = 5
    >>> sum = add_me(x, y)
    
    Notes
    -----
    Also function comments should use tripple quotes.
    """
    
    try:
        sum = x + y
        return sum
    except TypeError:
        print('The inputs of "add_me" are incompatible!')
    except:
        print('Something else went wrong.')


if __name__ == '__main__':
    # Here you can test your functions
    
    for a, b in zip([1, 2, 3], [1, np.arange(5), 'c']):
        print(f'trying to add {a} and {b}:')
        print(add_me(a,b))
