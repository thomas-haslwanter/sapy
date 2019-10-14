""" Calculation of confidence intervals """

# author:	Thomas Haslwanter
# date:		Oct-2019

# Import the required packages
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from pprint import pprint

# Gnerate the data
np.random.seed(123)
x = np.arange(100)
y = 30 + 0.4*x + 5*np.random.randn(len(x))

# Use a "DataFrame" to contain the data, and a "formula" to define the function
df = pd.DataFrame({'x':x, 'y':y})
formula = 'y~x'
results = smf.ols(formula, data=df).fit()

# Show the results, with the default 95% confidence intervals
print(results.summary())

# Address some of the fit-parameters
fit = {}
fit['parameters'] = results.params
fit['standard_error'] = results.bse
fit['ci_95'] = results.conf_int()               # 95%   confidence intervals
fit['ci_999'] = results.conf_int(alpha=0.001)   # 99.9% confidence intervals

for key in [key for key in fit.keys() if key.startswith('ci')]:
    print(f'{key}: {fit[key]}')
