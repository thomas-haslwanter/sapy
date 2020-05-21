""" Solution Exercise 12.x 'Simulation of Muscles' """

# author:   Thomas Haslwanter
# date:     April-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import control
from collections import namedtuple

# Define the paramters
r = 2
k = 1

# Generate the transfer functions for spring and damper
sys_spring = control.TransferFunction([k], [1])
sys_damper = control.TransferFunction([r,0], [1])

# Combine these for a Voigt-element, and for spring and damper in seial connection
voigt = 1/(control.parallel(sys_spring, sys_damper))
serial = 1/(control.series(sys_spring, sys_damper))

# Give the output simple names, and specify the time axis
Response = namedtuple('Response', ['t', 'x'])
t_out = np.arange(0,10,0.1)

# Simulate a step response of these two systems
r_voigt = Response(*control.step_response(voigt, t_out))
r_serial = Response(*control.step_response(serial, t_out))

# Plot the solutions
plt.plot(r_voigt.t, r_voigt.x, label='Voigt')
plt.plot(r_serial.t, r_serial.x, label='Serial')
plt.legend()
plt.xlabel('Time [sec]')
plt.ylabel('System Responses')
plt.show()
