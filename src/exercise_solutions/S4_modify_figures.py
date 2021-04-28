""" Solution to Exercise 'Modifying Figures', Chapter 'Data Display' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

# Set the positions of the figure elements
yi = 0.8
xi = 2*np.pi + np.arcsin(yi)
dx = 3
dy = 0.5

out_file = 'drawing.jpg'

# Generate the sine-wave
t = np.arange(0, 10, 0.1)
x = np.sin(t)

# Plot it
plt.plot(t,x)
plt.axhline(yi, ls='dotted')

# Annotate it
plt.annotate('This is\nnot funny!',
             xy = (xi,yi),
             xytext = (xi-dx, yi-dy),
             arrowprops=dict(facecolor='black', shrink=0.05) )
             
# Save JPG-file
pil_kwargs = {'quality': 90}
plt.savefig(out_file, dpi=200, pil_kwargs=pil_kwargs)

# Save the same file in SVG-format
svg_file = out_file.replace('jpg', 'svg')
plt.savefig(svg_file)
print(f'Saved {out_file} and {svg_file}')
plt.show()
plt.close()

# Now re-generate the plot in a "funny"-style, and save the file
# with "_funny" added to the JPG filename
with plt.xkcd():
    # Plot it 
    plt.plot(t,x)
    plt.axhline(yi, ls='dotted')
    
    # Annotate it
    plt.annotate('This is\nfunny!',
                 xy = (xi,yi),
                 xytext = (xi-dx, yi-dy),
                 arrowprops=dict(facecolor='black', shrink=0.05) )
                 
    funny_file = out_file.replace('.jpg', '_funny.jpg')
    plt.savefig(funny_file, dpi=200, pil_kwargs=pil_kwargs)
    print(f'... and also saved {funny_file} ;)')
    plt.show()
        
                
            
