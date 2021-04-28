""" Solution to Exercise 'Translation', the Chapter 'Python' """

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

# Define the original points
p_0 = [0,0]
p_1 = [2,1]

# Combine them to an array
array = np.array([p_0, p_1])
print(array)

# Translate the array
translated = array + [3,1]
print(translated)

# Plot the data
plt.plot(array[:,0], array[:,1], label='original')
plt.plot(translated[:,0], translated[:,1], label='translated')

# Format and show the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


