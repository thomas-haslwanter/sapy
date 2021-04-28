"""Common formatting and print commands, for the book "Hands-on Signal
Analysis with Python".
These commands ensure a common layout, and reduce the code required to
generate plots in the other modules.
"""

# Copyright(c) 2020, Thomas Haslwanter. All rights reserved, under
# the CC BY-SA 4.0 International License

# Import standard packages
import matplotlib.pyplot as plt
import os

# additional packages
import matplotlib as mpl


def set_fonts(fs=24):
    """Set my favorite defaulte fonts"""
    
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : fs}

    xtick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    ytick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}

    axes = {'labelsize': fs,
            'titlesize': fs}
    
    legend = {'fontsize': fs}
    
    figure = {'autolayout': False}
    
    mpl.rc('font', **font)
    mpl.rc('xtick', **xtick)
    mpl.rc('ytick', **ytick)
    mpl.rc('axes', **axes)
    mpl.rc('legend', **legend)
    mpl.rc('figure', **figure)
    
    
def show_data(out_file, out_dir = None):
    """Save a figure with subplots to a file, and then display it"""
    
    if out_dir is not None:
        # Generate the plot
        saveTo = os.path.join(out_dir, out_file)
        if out_file[-3:].lower() == 'jpg':
            plt.savefig(saveTo, dpi=200, quality=90)
        else:
            plt.savefig(saveTo, dpi=200)
    
        # Show the user where the file is saved to
        print('OutDir: {0}'.format(out_dir))
        print('Figure saved to {0}'.format(out_file))
    
    # Show the plot
    plt.show()
    plt.close()

    
if __name__ == '__main__':
    set_fonts()
    
    import numpy as np
    plt.plot(np.arange(5))    
    out_file = 'test.jpg'    
    show_data(out_file, out_dir = r'..\..\new_figures')
    
