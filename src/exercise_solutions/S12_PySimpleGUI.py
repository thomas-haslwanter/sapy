"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.

Basic steps are:
 * Create a Canvas Element
 * Layout form
 * Display form
 * Draw plots onto convas
 
Based on information from:
https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
"""

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


def make_sine(amp, freq, duration=2, dt=0.01):
    """Generate a Matplotlib-figure with a sinewave"""
    
    t = np.arange(0, duration, dt)
    omega = 2 * np.pi * freq
    x = amp * np.sin(omega * t)
    return t, x


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Matplotlib helper code """
    
    graph = FigureCanvasTkAgg(figure, master=canvas)
    graph.draw()
    listbox = graph.get_tk_widget()
    listbox.pack(side='top', fill='both', expand=1)
    return graph

if __name__ == '__main__':
    # Make the first plot
    t, x = make_sine(amp=1, freq=1)
    fig, ax = plt.subplots(1,1)
    ax.plot(t,x)
    
    ax.set_xlabel('Time [sec]')
    ax.set_ylabel('Sine-wave')
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

    # define the window layout
    layout = [[sg.Text('GUI-demo', font='Any 18')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.Text('Amplitude '), sg.InputText('1')],
              [sg.Text('Frequency'), sg.InputText('1')],
              [sg.Button('Ok'), sg.Button('Cancel')] ]
    
    # create the form and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI',
                       layout, finalize=True)
    
    # add the plot to the window
    graph = draw_figure(window['canvas'].TKCanvas, fig)
    
    event, values = window.read()
    while event == 'Ok':
        # Update the figure with the new parameters, until
        # the user hits "Cancel"
        amp = np.float(values[0])
        freq = np.float(values[1])
        t_new, x_new = make_sine(amp, freq)
        
        ax.cla()
        ax.plot(t_new, x_new)
        graph.draw()
        
        event, values = window.read()
    else:
        window.close()
