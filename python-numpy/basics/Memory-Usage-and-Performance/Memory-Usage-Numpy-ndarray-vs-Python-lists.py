# Memory Usage and Performance
# NumPy array vs Python List (memory usage)

import numpy as np
from sys import getsizeof                                           # gets the byte size of the element

# define a python list
_my_lst=[10,15,20,25, 30]                                           # Existing Python List

# create an numpy array based on this list
np_var=np.array(_my_lst)

print('size of existing python list in bytes: ', getsizeof(_my_lst))# size of existing python list in bytes:  120
print('size of numpy array in bytes: ', np_var.nbytes)              # size of numpy array in bytes:  16
print()
print('number of elements in numpy array: ', np_var.size)           # number of elements in numpy array:  5
print('size of elements in numpy array: ', np_var.itemsize)         # size of elements in numpy array:  4


# Output:
# size of existing python list in bytes:  120
# size of numpy array in bytes:  20

# number of elements in numpy array:  5
# size of elements in numpy array:  4