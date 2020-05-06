"""Solution to Exercise xxx of the chaper 'xxx' """

# author:   Thomas Haslwanter
# date:     May-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as mpl

def CorrVis(x:np.ndarray, y:np.ndarray) -> None:
    """Visualize correlation, by calculating the cross-correlation of two
    signals, one point at a time. The aligned signals and the resulting corss
    correlation value are shown, and advanced when the user hits a key or
    clicks with the mouse.
    
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
    """
    
    Nx = x.size
    Ny = y.size
    Nr = Nx + Ny -1
    
    xmin = -(Nx - 1)
    xmax = Ny + Nx -1
    
    if not 'fig' in locals():
        fig, axs = plt.subplots(3,1)
    # First plot: Signal 1
    axs[0].plot(range(Ny), y)
    ax = axs[0].axis()
    axs[0].axis([xmin, xmax, ax[2], ax[3]])
    axs[0].grid(True)
    axs[0].set_xticklabels(())
    axs[0].set_ylabel('Y[n]')
    
    # Precalculate limits of correlation output
    axr = [xmin, xmax, np.correlate(x,y,'full').min(), np.correlate(x,y,'full').max()]
    
    # Make a version of y padded to the full extent of X's we'll shift
    padY = np.r_[np.zeros(Nx-1), y, np.zeros(Nx-1)]
    Npad = padY.size
    R = []

    # Generate the cross-correlation, step-by-step
    for p in range(Nr):
        
        # Figure aligned X
        axs[1].cla()
        axs[1].plot(np.arange(Nx)-Nx+p+1, x)
        ax = axs[1].axis()
        axs[1].axis([xmin, xmax, ax[2], ax[3]])
        axs[1].grid(True)
        axs[1].set_ylabel('X[n-l]')
        axs[1].set_xticklabels(())
        
        # Calculate correlation
        # Pad an X to the appropriate place
        padX = np.r_[np.zeros(p), x, np.zeros(Npad-Nx-p)]
        R = np.r_[R, np.sum(padX * padY)]
        
        # Third plot: cross-correlation values
        axs[2].cla()
        axs[2].plot(np.arange(len(R))-(Nx-1), R, linewidth=2)
        axs[2].axis(axr)
        axs[2].grid(True)
        axs[2].set_ylabel('Rxy[l]')
        
        # Update the plot
        mpl.draw()
        mpl.waitforbuttonpress()
        
    mpl.show()

if __name__ == '__main__':
    x = np.r_[[0]*5, [1]*4, [0]*3]
    y = x
    CorrVis(x,y)
    
