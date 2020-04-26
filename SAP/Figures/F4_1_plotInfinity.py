"""Plot an infinity symbol"""

# author:   Thomas Haslwanter
# date:     March-2020

# Import all the standard packages
import numpy as np
import matplotlib.pyplot as plt

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

# Generate the trajectory
t = np.arange(0, 4*np.pi, 0.1)
x = np.sin(t)
y = np.sin(2*t)

plt.plot(x,y)
plt.plot(x[5], y[5], 'o', ms=10, color=[0,0,1,1])
plt.plot(x[4], y[4], 'o', ms=8, color=[0,0,1,0.3])
plt.plot(x[3], y[3], 'o', ms=6, color=[0,0,1,0.2])

plt.hlines(0, -1.2, 1.2, ls=':')
plt.vlines(0, -1.2, 1.2, ls=':')
plt.xlim([-1.2, 1.2])
plt.ylim([-1.2, 1.2])
plt.xlabel('X-position')
plt.ylabel('Y-position')

out_file = 'infinity.jpg'
show_data(out_file)
