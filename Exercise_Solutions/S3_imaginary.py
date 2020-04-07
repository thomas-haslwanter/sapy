"""Solution to Exercise 3 of the chaper 'Data IO' """

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set the required parameters
in_file = r'..\Data\imaginary.txt'
out_file = 'imaginary_out.txt'

# Get the data
df = pd.read_csv(in_file, delim_whitespace=True)

# Add radius and angle as new columns
df['Radius'] = np.sqrt(df.Real**2 + df.Imaginary**2)
df['Angle [rad]'] = np.arctan2(df.Imaginary, df.Real)

# Make sure all columns are floats, and write to the new file
df = df.astype('float')
df.to_csv(out_file, sep='\t', index=None, float_format='%5.3f')
print(f'Modified data saved to {out_file}')