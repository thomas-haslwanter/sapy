""" Use the Python-package 'control' to implement a feedback loop """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import control

# Define the transfer function - a first order lag, with tau=5 sec
num = 1
den = [5, 1]
sys = control.TransferFunction(num, den)
print(sys)

# Define the input, a step at t=1
t = np.arange(0, 25, 0.1)
in_signal = np.zeros_like(t)
in_signal[t>1] = 1

# simulate the response
t_out, y_out, x_out = control.forced_response(sys, T=t, U=in_signal)
plt.plot(t, in_signal, '-', label='Input')
plt.plot(t_out, y_out, '--', label='Feedforward')

# Define a feedback-loop, with gain k
k = 2
sys_total = control.feedback(sys, k)
print(sys_total)
t_total, y_total, x_total = control.forced_response(sys_total, T=t, U=in_signal)
plt.plot(t_total, y_total, '-.', label='Feedback')
plt.legend()

out_file = 'feedback.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
