""" Show different ways to present statistical data.

The examples contain:
- scatter plots, with 1-dimensional and higher-dimensional data
- histograms
- boxplots
- errorbars
- barplots
- grouped boxplots
- pieplots
- scatterplots, with markersize proportional to the value of a corresponding variable
- 3D surface and wireframe plots
"""

# author:   Thomas Haslwanter
# date:     June-2020

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd
import os

# additional packages
import matplotlib as mpl
from utilities.my_style import set_fonts, show_data 

    
def printout(outFile: str, xlabel: str='', ylabel: str='',
             title: str='', outDir: str='.') -> None:
    """Save the current figure to a file, and then display it."""
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.tight_layout
    
    xlim = plt.gca().get_xlim()
    plt.hlines(0, xlim[0], xlim[1], linestyles='--', colors='#999999')
    plt.gca().set_xlim(xlim)
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()
    
    
def simplePlots() -> None:
    """ Demonstrate the generation of different statistical standard plots. """
    
    # Univariate data -------------------------
    
    # Make sure that always the same random numbers are generated
    np.random.seed(1234)
    
    # Generate data that are normally distributed
    x = np.random.randn(500)
    
    # Other graphics settings
    # Set " context='poster' " for printouts, and "set_fonts(32)"
    sns.set(context='notebook', style='ticks', palette='muted')
    
    # Set the fonts the way I like them
    set_fonts(16)
    
    # Scatter plot
    plt.plot(x, '.', markersize=7)
    plt.xlim([0, len(x)])
    
    # Save and show the data, in a systematic format
    printout('scatterPlot.jpg', xlabel='Datapoints', ylabel='Values', title='Scatter')
    
    # Histogram
    plt.hist(x)
    printout('histogram_plain.jpg', xlabel='Data Values',
             ylabel='Frequency', title='Histogram, default settings')
    
    plt.hist(x, 25, density=True)
    printout('density_histogram.jpg', xlabel='Data Values', ylabel='Probability',
             title='Density Histogram, 25 bins')
    
    # Boxplot
    # The ox consists of the first, second (middle) and third quartile
    plt.boxplot(x, sym='*')
    printout('boxplot.jpg', xlabel='Values', title='Boxplot')
    
    plt.boxplot(x, sym='*', vert=False)
    plt.title('Boxplot, horizontal')
    plt.xlabel('Values')
    plt.show()
    
    # Errorbars
    x = np.arange(5)
    y = x**2
    errorBar = x/2
    plt.errorbar(x,y, yerr=errorBar, fmt='o', capsize=5, capthick=3)
    plt.xlim([-0.2, 4.2])
    plt.ylim([-0.2, 19])
    printout('Errorbars.jpg', xlabel='Data Values', ylabel='Measurements', title='Errorbars')

    # SD for two groups
    weight = {'USA':89, 'Austria':74}
    weight_SD_male = 12
    plt.errorbar([1,2], weight.values(), yerr=weight_SD_male * np.r_[1,1],
     capsize=5, LineStyle='', marker='o')
    plt.xlim([0.5, 2.5])
    plt.xticks([1,2], weight.keys())
    plt.ylabel('Weight [kg]')
    plt.title('Adult male, mean +/- SD')

    show_data('SD_groups.jpg')
    
    # Barplot
    # The font-size is set such that the legend does not overlap with the data
    np.random.seed(1234)
    set_fonts(16)
    
    df = pd.DataFrame(np.random.rand(7, 3), columns=['one', 'two', 'three'])
    df.plot(kind='bar', grid=False, color=sns.color_palette('muted'))
    
    show_data('barplot.jpg')

    # Bivariate Plots
    df2 = pd.DataFrame(np.random.rand(50, 3), columns=['a', 'b', 'c'])
    df2.plot(kind='scatter', x='a', y='b', s=df2['c']*500);
    plt.axhline(0, ls='--', color='#999999')
    plt.axvline(0, ls='--', color='#999999')
    printout('bivariate.jpg')
    
    sns.set_style('ticks')

    # Pieplot
    txtLabels = 'Cats', 'Dogs', 'Frogs', 'Others'
    fractions = [45, 30, 15, 10]
    offsets =(0, 0.05, 0, 0)
    
    plt.pie(fractions, explode=offsets, labels=txtLabels,
            autopct='%1.1f%%', shadow=True, startangle=90,
            colors=sns.color_palette('muted') )
    plt.axis('equal')
    printout('piePlot.jpg', title=' ')

    
def show3D() -> None:
    """ Generate 3D plots. """
    
    # imports specific to the plots in this example
    from matplotlib import cm   # colormaps
    
    # This module is required for 3D plots!
    from mpl_toolkits.mplot3d import Axes3D
    
    # Twice as wide as it is tall.
    fig = plt.figure(figsize=plt.figaspect(0.5))
    set_fonts(16)
    
    #---- First subplot
    # Generate the data
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    # Note the definition of "projection", required for 3D  plots
    #plt.style.use('ggplot')

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.GnBu,
            linewidth=0, antialiased=False)
    #surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis_r,
            #linewidth=0, antialiased=False)
    ax.set_zlim3d(-1.01, 1.01)
    
    fig.colorbar(surf, shrink=0.5, aspect=10)
    
    #---- Second subplot
    # Get some 3d test-data
    from mpl_toolkits.mplot3d.axes3d import get_test_data
    
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

    show_data('3dGraph.jpg')
    
    
if __name__ == '__main__':
    simplePlots()
    show3D()
