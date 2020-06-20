"""Solution to Exercise 'First Steps with Pandas' of the chapter 'Python' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set the parameters
rate =  10
start, stop = 0, 10
freq = 1.5
out_file = 'out.txt'

# Calculate the data
dt = 1/rate
omega = 2*np.pi*freq

x = np.arange(start, stop, dt)
y = np.sin(omega*x)
z = np.cos(omega*x)

# Put them into a pandas DataFrame
df = pd.DataFrame({'Time': x, 'YVals': y, 'ZVals': z})

# Show the head
print(df.head())

# Extract rows 10-15. Be careful with the last row!
data = df[ ['YVals', 'ZVals'] ][10:16]

# Write them to the out-file
data.to_csv(out_file)
print(f'Data have been written to {out_file}')
