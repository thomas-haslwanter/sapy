""" Show import from data with Matlab
The data were generated with the following Matlab commands:
    int_number = 42;
    float_number = pi;
    my_vector = 0:0.1:10;
    my_matrix = randi(9, 4, 3);
    my_text = 'This is for Jean';
    my_cell = {'This is the value of pi', pi, 0:0.1:1}
    my_struct.info = 'This is a structure-text';
    my_struct.data = my_vector;
    save data
"""

# author:   Thomas Haslwanter
# date:     April-2021

# Import the required libraries
import numpy as np


def m4py(in_file: str) -> dict:
    """ Solution with mat4py """
    
    import mat4py
    
    data = mat4py.loadmat(in_file)
    for key, value in data.items():
            print(f'{key} = {value}')
            
    # For numerical work, lists have to be converted to arrays:
    array_data = np.array( data['my_struct']['data'] )
    print(array_data)
    
    return data
        
    
def scipy_matlab(in_file: str) -> dict:
    """ Solution with scipy only """
    
    from scipy.io import loadmat
    
    # For numbers, vectors, matrices, and cells, the option 'squeeze_me'
    # is helpful, to simplify the format
    data = loadmat(in_file, squeeze_me=True)
    
    int_number = data['int_number']
    float_number = data['float_number']
    my_vector = data['my_vector']
    my_matrix = data['my_matrix']
    my_text = data['my_text']
    
    my_cell = []
    for ii in range(len(data['my_cell'])):
            my_cell.append( data['my_cell'][ii] )
    
    # For structures where you know the fields, you can address them directly
    my_structure = {}
    for field in ['info', 'data']:
            my_structure[field] = data['my_struct'][field].item()
            
    for elements in ['int_number', 'float_number', 'my_vector', 'my_matrix', \
            'my_text', 'my_cell', 'my_structure']:
            print(f'{elements} = {eval(elements)}')
            
    print('--------------------')        
    
    # If you don't know the fields, the best I can do is        
    data2 = loadmat(matlab_file) # sets the default 'squeeze_me=False'
    
    struct_values = data2['my_struct'][0,0][0][0]
    struct_string = data2['my_struct'][0,0][1][0]
    
    my_struct = []
    for ii in range(len(data2['my_struct'][0,0])):
            my_struct.append( data2['my_struct'][0,0][ii] )
    
    print(my_struct) 
    my_struct_fields = data2['my_struct'][0].dtype
    print(f'my_struct_fields = {my_struct_fields}')
    
    return data

    
if __name__ == '__main__':
    matlab_file = r'..\..\data\data.mat'
    
    m4py_data = m4py(matlab_file)    
    scipy_data = scipy_matlab(matlab_file)    
    
    # Just to check the output
    data = np.array(m4py_data['my_matrix'])    
    print(data)    
    print(scipy_data['my_matrix'])
