import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

xx = np.zeros(20)
xx[5] = 1
tt = np.arange(20)

data = {}
data['before'] = xx
data['after_fir'] = signal.lfilter(np.ones(5)/5, 1, xx)
data['after_iir'] = signal.lfilter([1], [1, -0.5], xx)

plt.plot(tt, data['before'], 'bo', label='input', lw=2)
plt.plot(tt, data['after_fir'], 'rx-', label='FIR-filtered', lw=2)
plt.plot(tt, data['after_iir'], 'b.:', label='IIR-filtered', lw=2)

plt.legend()
plt.xlim([0, 20])
plt.xticks(np.arange(0, 20, 2))
plt.show()