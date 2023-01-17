# How to create an NumPy Array
# Creation of NumPy single-dimension array
# array() :- for creation of single array from an existing python list

import numpy as np
_my_lst=[10,15,20,25]                  # Existing Python List

np_var=np.array(_my_lst)               # using array() on existing python list
print('np_var: ', np_var)              # np_var: [10 15 20 25]
print('np_var type: ', type(np_var))   # np_var type: <class'numpy.ndarray'> :- ndarray = n-dimensional array

# Output
# np_var:  [10 15 20 25]
# np_var type:  <class 'numpy.ndarray'>