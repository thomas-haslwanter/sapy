"""Addition to Exercise 1 of the chaper 'Data IO'
It shows how to generate
- formatted text-strings
- CSV files
- otherwise formmated TXT-files
- Excel files
- Matlab files
"""

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set the parameters for a sine wave
rate = 50
freq = 2
duration  = 4
amp = 5
noise_amp = 0.8

# Calculate the sine-values
delta = np.deg2rad(15)
dt = 1/rate
omega = 2*np.pi*freq

t = np.arange(0, duration, dt)
data = amp * np.sin(omega*t + delta) + noise_amp * np.random.randn(len(t))

# Put them in a pandas-DataFrame, for easier text output
df = pd.DataFrame({'t':t, 'values':data})

# Show how to generate a formatted string in Python
print(f'The first time-sample is {t[0]:5.3f}, and the first data-value is {data[0]:5.3f}')

# Saves the data to CSV-format, which means by default
# - Separated by a comma
# - With a column name
# - With a running index on the left side
csv_file = 'data.csv'
df.to_csv(csv_file)

# Always let the user know when you generate a new file!!
# If you use Python >3.7, you can use the "format-strings"
print(f'Data have been saved in CSV-format to {csv_file}')

# For earlier versions of Python you have to use
print('Data have been saved in CSV-format to {0}'.format(csv_file))

# Simple file, tab-separated, no header, no index
simple_file = 'data_tab.txt'
df.to_csv(simple_file, sep='\t', header=False, index=False)
print(f'Data have been saved to {simple_file}')

# Show how to add a file-header to an existing text file
with open(csv_file, 'r') as original:
    text = original.read()
    
modified_file = 'data_modified.txt'    
with open(modified_file, 'w') as modified:
    modified.write('This file was generated on Sept 19\n')
    modified.write(f'Sampling rate: {rate} [Hz]\n')
    modified.write(text)
print(f'A file header has been added to {csv_file}, and the new file saved as {modified_file}')

# Save data to Excel-format
excel_file = 'data.xls'
df.to_excel(excel_file, index=False)
print(f'Data have been saved in MS-Excel format, to {excel_file}')

# To save data to Matlab-format, we need the package "scipy.io", ...
from scipy.io import savemat

# ... and we have to put the data into a Python-dictionary
# For this example, I add an information-text, and format the data as a matrix
data_mat = np.column_stack( (t, data) )
data_dict = {'info':'These are demo-data, showing a sine-wave',
            'data': data_mat}

matlab_file = 'data.mat'
savemat(matlab_file, data_dict)
print(f'Data have been saved in Matlab format, to {matlab_file}')

