"""Solution to Exercise xxx of the chaper 'xxx' """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt


def add_one(data):
    """Adds '1' to the given data"""
    added = data[:,0] +1 
    return added


def BrokenMethod(strInput):
    """From https://docs.fuzzbuzz.io/
    Returns 'True' for strings like 'FUZZBUZZ', 'False' for most other strings
    """
    
    if len(strInput) >= 1:
        return strInput[0] == 'F' and strInput[1] == 'U'# and strInput[2] == 'Z' 
    

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
    
   
    
    
