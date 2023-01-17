# How to convert a NumPy array to a Python list
# tolist() method

import numpy as np

np_var=np.array([10,15,20,25] )                 # using array() to create an numpy array from list of elements
print('np_var: ', np_var)                       # np_var: [10 15 20 25]
print('np_var type: ', type(np_var))            # np_var type: <class'numpy.ndarray'> :- ndarray = n-dimensional array

_my_py_lst=np_var.tolist()
print('_my_py_lst: ', _my_py_lst)               # _my_py_lst:  [10, 15, 20, 25]
print('_my_py_lst type: ', type(_my_py_lst))    # _my_py_lst type:  <class 'list'>


# Output
# np_var:  [10 15 20 25]
# np_var type:  <class 'numpy.ndarray'>
# _my_py_lst:  [10, 15, 20, 25]
# _my_py_lst type:  <class 'list'>