""" Trigger an error that can be investigated with a debugger. """

# author:   Thomas Haslwanter
# date:     May-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt


def add_one(data : np.ndarray) -> np.ndarray:
    """Adds '1' to the given data
    
    Parameters
    ----------
    data : numerical input; can be float or np.ndarray

    Returns
    -------
    added : 'data' + 1
    """

    added = data[:,0] +1 
    return added


def BrokenMethod(input_str : str) -> bool:
    """ Return 'True' for strings like 'FUZZBUZZ', 'False' for most other strings
    From https://docs.fuzzbuzz.io/

    Parameters
    ----------
    input_str : some string

    Returns
    -------
    is_fuzzy : True if the string starts with 'FU...'; False otherwise
    """
    
    if len(input_str) >= 1:
        return input_str[0] == 'F' and input_str[1] == 'U'# and input_str[2] == 'Z' 
    

def FuzzerEntrypoint(Data):
    """From https://docs.fuzzbuzz.io/ """
    
    try:
        strData = str(Data.read(), "utf-8")
        return BrokenMethod(strData)
        
    except UnicodeDecodeError:
        return None
    
    
if __name__ == '__main__':
    
    t = np.arange(0, 10, 0.1)
    x = np.sin(tt)
    
   
    
    
