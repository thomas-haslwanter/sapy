% Generates and saves different Matlab data-structures
%
% Author:   Thomas Haslwanter
% Date:     April-2021

int_number = 42;
float_number = pi;
my_vector = 0:0.1:10;
my_matrix = randi(9, 4, 3);
my_text = 'This is for Jean';
my_cell = {'This is the value of pi', pi, 0:0.1:1}
my_struct.info = 'This is a structure-text';
my_struct.data = my_vector;
save data