"""Solution to Exercise 3 of the chaper 'Data IO' """

# author:   Thomas Haslwanter
# date:     April-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set the required parameters
data_dir = r'..\..\Data'
file_name = 'imaginary.txt'
in_file = os.path.join(data_dir, file_name)
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
