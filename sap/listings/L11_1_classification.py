""" Simple classification model for "iris" data-set """

# author:   Thomas Haslwanter
# date:	    May-2020

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ... and the data and functions needed from scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from utilities.SAP_mystyle import set_fonts, show_data 

# Load the data
iris_dataset = load_iris()

# Show misc data information
print(f'Keys of iris_dataset: {iris_dataset.keys()}')
print(iris_dataset['DESCR'])
print(f"Target names: {iris_dataset['target_names']}")
print(f"Feature names: {iris_dataset['feature_names']}")
print(f"Shape of data: {iris_dataset['data'].shape}")
print(f"First 5 rows of data:\n {iris_dataset['data'][:5]}")

# Split data into training- and test-set
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# Define and train the network
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Show how accurate it is
print(f'Test set score: {knn.score(X_test, y_test):.2f}')

# Plot the data ----------------------------
# First bring the data into a pandas DataFrame, and group them by "species"
plot_data = np.column_stack( (X_train, y_train) )
df = pd.DataFrame(data=plot_data,
                  columns=['Prop_1', 'Prop_2', 'Prop_3', 'Prop_4', 'species'])
groups = df.groupby('species')

# Plot the groups
fig, axs = plt.subplots(1,2)
for name, group in groups:
    axs[0].plot(group.Prop_1, group.Prop_2, 'o')
    axs[1].plot(group.Prop_3, group.Prop_4, 'o')
    
axs[0].set_xlabel('Property 1')
axs[0].set_ylabel('Property 2')
axs[1].set_xlabel('Property 3')
axs[1].set_ylabel('Property 4')    

# Take an arbitrary new sample, and plot it
new_sample = np.array([[7, 3.5, 6, 2]])
axs[0].plot(*new_sample[0,:2], 'r+', ms=18)
axs[1].plot(*new_sample[0,-2:], 'r+', ms=18)

axs[1].legend( list(iris_dataset['target_names']) + ['predicted'],
               loc='upper left')    

# Classify it, and show the result
classified = knn.predict(new_sample)
plt.text(3, 0.1, f"Predicted: {iris_dataset['target_names'][classified]}")

plt.tight_layout()
out_fig = 'ml_classified.jpg'
show_data(out_fig)
