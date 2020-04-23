"""Simulate the measurement effect of a shift of the sampling location"""

# author:   Thomas Haslwanter
# date:     April-2020

import numpy as np
import matplotlib.pyplot as plt

def find_pattern(arc):
    amp_freq_phase = [[1, 10, 0.12],
                      [1, 20, 0.22],
                      [0.7, 45, 0.32],
                      [0.7, 70, 0.42],
                      [0.4, 110, 0.1],
                      [0.3, 150, 0.2]]                  

    n_pts = len(arc)
    pattern = np.zeros(n_pts)
    for params in amp_freq_phase:
        amp, freq, phase = params
        pattern += amp*np.sin(freq*arc + phase)    
        
    # normalize the pattern
    pattern_range = np.max(pattern) - np.min(pattern)
    pattern /= pattern_range
    pattern -= np.mean(pattern)
    return pattern


if __name__ =='__main__':
    
    # amplitudes and frequencies for the iris simulation
    num_pts = 256
    arc_length = 60             # [deg]
    arc_start = 10
    arc_deg = np.linspace(arc_start, arc_start + arc_length, num_pts)
    delta = np.diff(arc_deg[:2])
    arc = np.deg2rad(arc_deg)
    
    pattern = find_pattern(arc)
    
    deg = arc_start + delta * np.arange(num_pts)
    
    # Simulate the pattern when looking into an eccentric eye position
    # Here I assume that the iris is flat, and ignore distorsions by
    # the cornea
    alpha_deg = 30      # deg
    alpha = np.deg2rad(alpha_deg)
    
    arc_new = np.ones_like(arc) * np.nan
    for (ii, angle) in enumerate(arc):
        y = np.sin(angle)
        x = np.cos(angle)/np.cos(alpha)
        arc_new[ii] = np.arctan2(y,x)
        
    pattern_new = find_pattern(arc_new)
    
    # Plot the auto- and the cross-correlation
    auto_correlation = np.correlate(pattern, pattern, mode='full')
    cross_correlation = np.correlate(pattern, pattern_new, mode='full')
    deg_lag = np.arange(-num_pts+1, num_pts) * delta
    
    # Make the figure
    fig, axs = plt.subplots(2,1, figsize=(6.4, 6.4))   # default size: (6.4,4.8)
    
    axs[0].plot(deg_lag, auto_correlation, label='Auto-correlation')
    axs[0].plot(deg_lag, cross_correlation, '--', label='Cross-correlation')
    axs[0].legend()
    #axs[0].set_title('Auto-correlation and uncompensated cross-correlation')
    axs[0].set_xlabel('Shift [deg]')
    
    axs[1].plot(deg, pattern, label='Original pattern')    
    axs[1].plot(deg, pattern_new, '--', label='Shifted pattern')
    axs[1].legend(loc='upper right')
    #axs[1].set_title('Iral signatures')
    axs[1].set_xlabel('Arc-position [deg]')
    
    fig.tight_layout()
    
    out_file = 'simulation_iral_pattern_square.jpg'
    plt.savefig(out_file, dpi=200, quality=90)
    print(f'Image saved to {out_file}')
    plt.show()
