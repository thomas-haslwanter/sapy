""" 
Simple classification model for "iris" data-set
"""

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt

# ... and the data and functions needed from scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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
