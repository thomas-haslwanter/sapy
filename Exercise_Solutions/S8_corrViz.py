"""Solution to Exercise xxx of the chaper 'xxx' """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
'''
Visualize correlation, by calculating the cross-correlation of two signals, one point at a time.
The aligned signals and the resulting corss correlation value are shown, and advanced when the user
hits a key or clicks with the mouse.

Parameters
----------
X : Comparison signal
Y : Reference signal

Example
-------
x = np.r_[0:2*pi:10j]
y = sin(x)
CorrVis(y,y)

Notes
-----
Based on an idea from dpwe@ee.columbia.edu

Author : Thomas Haslwanter
Version : 1.0
Date : Sept-2012

'''
import numpy as np
import matplotlib.pyplot as mpl

def CorrVis(x,y):
    ''' Visualize how the values of a cross-correlation get generated '''
    Nx = x.size
    Ny = y.size
    Nr = Nx + Ny -1
    
    xmin = -(Nx - 1)
    xmax = Ny + Nx -1
    
    # First plot: Signal 1
    ax1 = mpl.subplot(311)
    ax1.plot(range(Ny), y)
    ax = ax1.axis()
    ax1.axis([xmin, xmax, ax[2], ax[3]])
    ax1.grid(True)
    ax1.set_xticklabels(())
    ax1.set_ylabel('Y[n]')
    
    # Precalculate limits of correlation output
    axr = [xmin, xmax, np.correlate(x,y,'full').min(), np.correlate(x,y,'full').max()]
    
    # Make a version of y padded to the full extent of X's we'll shift
    padY = np.r_[np.zeros(Nx-1), y, np.zeros(Nx-1)]
    Npad = padY.size
    R = []

    # Generate the cross-correlation, step-by-step
    for p in range(Nr):
        
        # Figure aligned X
        ax2 = mpl.subplot(312)
        ax2.hold(False)
        ax2.plot(np.arange(Nx)-Nx+p+1, x)
        ax = ax2.axis()
        ax2.axis([xmin, xmax, ax[2], ax[3]])
        ax2.grid(True)
        ax2.set_ylabel('X[n-l]')
        ax2.set_xticklabels(())
        
        # Calculate correlation
        # Pad an X to the appropriate place
        padX = np.r_[np.zeros(p), x, np.zeros(Npad-Nx-p)]
        R = np.r_[R, np.sum(padX * padY)]
        
        # Third plot: cross-correlation values
        ax3 = mpl.subplot(313)
        ax3.hold(False)
        ax3.plot(np.arange(len(R))-(Nx-1), R, linewidth=2)
        ax3.axis(axr)
        ax3.grid(True)
        ax3.set_ylabel('Rxy[l]')
        
        # Update the plot
        mpl.draw()
        mpl.waitforbuttonpress()
        
    mpl.show()

if __name__ == '__main__':
    x = np.r_[[0]*5, [1]*4, [0]*3]
    y = x
    CorrVis(x,y)
    
