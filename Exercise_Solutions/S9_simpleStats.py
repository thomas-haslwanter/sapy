""" Solution Exercise 9.3 'Statistical data analysis'
"""

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy import stats


def generate_and_analyze():
    """Task1: Generate and analyze the data, and return them"""
        
    # Generate the data ...
    np.random.seed(12345)   # Ensure reproducability
    num_data = 100
    group1, group2, group2_after = {},{},{}
    group1['data'] = 8 * random.randn(num_data) + 60
    group2['data'] = 10* random.randn(num_data) + 55
    group2_after['data'] = group2['data'] + 0.25 + 1*random.randn(num_data)
    
    
    # ... and analyze them
    group1_10 = {'data':group1['data'][:10],
                'mean':np.mean(group1['data'][:10]),
                 'std': np.std(group1['data'][:10], ddof=1),
                 'sem': stats.sem(group1['data'][:10]) }
    
    group1 = {'data':group1['data'],
              'mean':np.mean(group1['data']),
              'std': np.std(group1['data'], ddof=1),
              'sem': stats.sem(group1['data']) }
    
    group2 = {'data':group2['data'],
              'mean':np.mean(group2['data']),
              'std': np.std(group2['data'], ddof=1),
              'sem': stats.sem(group2['data']) }
    
    return (group1, group1_10, group2, group2_after)


def show(data):
    """Show errorplots with SD and SEM, and a boxplot of the data"""
    
    # Unravel the data
    (group1, group1_10, group2, group2_after) = data
    
    fig, axs = plt.subplots(1,3)
    
    # The first two plots show SDs and SEMs ...
    ylims = [30, 90]
    for ii, param in enumerate(['std', 'sem']):
        axs[ii].errorbar([1,2], [group1['mean'], group2['mean']], yerr=[group1[param], group2[param]], fmt='o g')
        axs[ii].set_xlim([0.5, 2.5])
        axs[ii].set_ylim(ylims)
        axs[ii].set_xticks([1,2])
        axs[ii].set_xticklabels(['Group1', 'Group2'])
        axs[ii].set_title('Errorbars: '+param)
    
    axs[0].set_ylabel('Weight [kg]')
    axs[1].set_yticklabels([])
    
    # ... and then the boxplots 
    data = [group1['data'], group2['data']]
    axs[2].boxplot(data)
    axs[2].set_xticks([1,2])
    axs[2].set_xticklabels(['Group1', 'Group2'])
    axs[2].set_ylim(ylims)
    axs[2].set_yticklabels([])
    axs[2].set_title('Boxplot')
    
    plt.show()


def compare(data):
    """ Compare groups """
    
    # Unravel the data
    (group1, group1_10, group2, group2_after) = data
     
    _,p = stats.ttest_ind(group1['data'], group2['data'])
    if p < 0.05:
        print('There is a significant difference between group1 and group2.')
    else:
        print('No significant difference between Group1 and Group2.')
    
    _,p = stats.ttest_rel(group2['data'], group2_after['data'])
    if p < 0.05:
        print('The carb diet causes a significant weight change.')
    else:
        print('The carb diet causes NO significant weight change.')
    

if __name__ == '__main__':
    
    data = generate_and_analyze()
    show(data)
    compare(data)
