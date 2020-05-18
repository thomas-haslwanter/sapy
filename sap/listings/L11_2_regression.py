"""
=============================================
Comparison of kernel ridge regression and SVR
=============================================

Both kernel ridge regression (KRR) and SVR learn a non-linear function by
employing the kernel trick, i.e., they learn a linear function in the space
induced by the respective kernel which corresponds to a non-linear function in
the original space. They differ in the loss functions (ridge versus
epsilon-insensitive loss). In contrast to SVR, fitting a KRR can be done in
closed-form and is typically faster for medium-sized datasets. On the other
hand, the learned model is non-sparse and thus slower than SVR at
prediction-time.

This example illustrates both methods on an artificial dataset, which
consists of a sinusoidal target function and strong noise added to every fifth
datapoint. The first figure compares the learned model of KRR and SVR when both
complexity/regularization and bandwidth of the RBF kernel are optimized using
grid-search. The learned functions are very similar; however, fitting KRR is
approx. seven times faster than fitting SVR (both with grid-search). However,
prediction of 100000 target values is more than tree times faster with SVR
since it has learned a sparse model using only approx. 1/3 of the 100 training
datapoints as support vectors.

"""

# Authors: original code by Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>;
#          code elements extracted by Thomas Haslwanter
# License: BSD 3 clause

# Import the required packages
import numpy as np
import time

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge
import matplotlib.pyplot as plt

# #############################################################################
# Generate sample data
rng = np.random.RandomState(0)
X = 5 * rng.rand(10000, 1)
y = (np.sin(2*X)**2/X).ravel()

# Add noise to targets
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]

# #############################################################################
# Fit regression model
train_size = 100
svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
                   param_grid={"C": [1e0, 1e1, 1e2, 1e3],
                               "gamma": np.logspace(-2, 2, 5)})

kr = GridSearchCV(KernelRidge(kernel='rbf', gamma=0.1), cv=5,
                  param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                              "gamma": np.logspace(-2, 2, 5)})

svr.fit(X[:train_size], y[:train_size])
kr.fit(X[:train_size], y[:train_size])

y_svr = svr.predict(X_plot)
y_kr = kr.predict(X_plot)

# #############################################################################
# Look at the results
sv_ind = svr.best_estimator_.support_
plt.scatter(X[:200], y[:200], c='C0', label='data', zorder=1)
plt.plot(X_plot, y_kr, c='C0', label='KRR')

plt.scatter(X[sv_ind], y[sv_ind], c='C1', s=50, label='SVR support vectors',
            zorder=2 )
plt.plot(X_plot, y_svr, c='C1', label='SVR ')

plt.xlabel('Regressor')
plt.ylabel('Predicted Variable')
plt.title('SVR versus Kernel Ridge')
plt.legend()

# To save to an out-file with my default formatting
out_file = 'fit_regression.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
