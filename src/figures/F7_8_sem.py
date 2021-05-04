""" Scatterplot of normally distributed data, with SD and Standard Error """

# author:   Thomas Haslwanter
# date:     April-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Import formatting commands 
from utilities.my_style import set_fonts, show_data 


def arrow_bidir(ax, start, end, headWidth=0.01):
    """Plot a bidirectional arrow"""
    
       # For the arrow, find the start
       
    start = np.array(start)
    end = np.array(end)
    delta = end - start
    
    ax.arrow(start[0], start[1], delta[0], delta[1],
              width=headWidth, length_includes_head=True,
              head_length=headWidth*3, head_width=headWidth*5, color='k')
    
    ax.arrow(end[0], end[1], -delta[0], -delta[1],
              width=headWidth, length_includes_head=True,
              head_length=headWidth*3, head_width=headWidth*5, color='k')


if __name__ == '__main__':    
    # Generate the data
    np.random.seed(123)
    x = np.random.randn(150) + 5

    # Calculate "standard devation" and "standard error" locations
    sdVal = np.std(x, ddof=1)
    seVal = stats.sem(x)
    sd = np.mean(x) + sdVal*np.r_[-1, 1]
    se = np.mean(x) + seVal*np.r_[-1, 1]

    # Set up the plot
    set_fonts(12)

    # Plot the data
    plt.plot(x,'.', ms=5)
    plt.axhline(np.mean(x), color=0.7*np.ones(3))
    plt.axhline(sd[0], ls='--', color='C0')
    plt.axhline(sd[1], ls='--', color='C0')

    # Lines for SEM
    lh = []
    lh.append( plt.axhline(se[0], ls='--', color='C1') )
    lh.append( plt.axhline(se[1], ls='--', color='C1') )

    # make the lines long-dashed
    dashes = [8, 2] # 8 points on, 2 off
    for ii in range(len(lh)):
        lh[ii].set_dashes(dashes)

    curAxis = plt.gca()
    curAxis.set_xticklabels( () )

    # Make the arrows
    plt.arrow(10, np.mean(x), 0, sdVal,
        width=0.2, length_includes_head=True,
        head_length=0.1, head_width=2, color='k')

    plt.arrow(10, np.mean(x), 0, -sdVal,
        width=0.2, length_includes_head=True,
        head_length=0.1, head_width=2, color='k')

    plt.arrow(60, np.mean(x)-4*seVal, 0, 3*seVal,
        width=0.2, length_includes_head=True,
        head_length=0.1, head_width=2, color='k')

    plt.arrow(60, np.mean(x)+4*seVal, 0, -3*seVal,
        width=0.2, length_includes_head=True,
        head_length=0.1, head_width=2, color='k')

    # Add the text
    fs = 18
    plt.text(11, 5.5, '$\pm$ 1SD', fontsize=fs, 
             fontstyle='italic', color='C0')
    plt.text(62, 5.2, '$\pm$ 1SEM', fontsize=fs, 
             fontstyle='italic', color='C1')

    # plt.annotate('mean', (110,np.mean(x)),xycoords='data',
    #         fontsize=fs, xytext=(110, 5.5), textcoords='data',
    #         arrowprops={
    #             'facecolor':'black',
    #             'shrink':1,
    #             'headwidth':6,
    #             'headlength':6,
    #             'width': 1})

    plt.annotate('mean', (-5,np.mean(x)),xycoords='data',
            fontsize=fs, xytext=(-40, 4.5), textcoords='data',
            color = [0.6, 0.6, 0.6],
            arrowprops={
                'color':[0.6, 0.6, 0.6],
                'shrink':1,
                'headwidth':6,
                'headlength':6,
                'width': 1})

    # Save and show
    plt.tight_layout()
    outFile = 'standardError.jpg'
    show_data(outFile, out_dir='.')
