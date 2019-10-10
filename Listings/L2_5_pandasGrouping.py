""" Demonstration of how to use the 'grouping' method for Pandas DataFrames """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Gender': ['f', 'f', 'm', 'f', 'm',
                'm', 'f', 'm', 'f', 'm', 'm'],
    'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,
                 5.1, 3.9, 3.7, 2.1, 4.3]
    })

#--------------------------------------------
# Group the data
grouped = data.groupby('Gender')

# Do some overview statistics
print(grouped.describe())

# Plot the data:
grouped.boxplot()
plt.show()

#--------------------------------------------
# Get the groups as DataFrames
df_female = grouped.get_group('f')

# Get the corresponding numpy-array
values_female = grouped.get_group('f').values

