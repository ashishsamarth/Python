# Memory Usage and Performance
# NumPy array vs Python List (memory usage)
# With default and specific data types

import numpy as np
from sys import getsizeof                                               # gets the byte size of the element

# define a python list
_my_lst=list(range(1000))                                               # Existing Python List

# create an numpy array based on this list with default datatype - int32
np_var_int_32=np.array(_my_lst)

# create an numpy array based on this list with sepcific datatype - int16
np_var_int_16=np.array(_my_lst, dtype=np.int16)

print('size of existing python list in bytes: ', getsizeof(_my_lst))     # size of existing python list in bytes:  8056
print('size of np_var_int_32 in bytes: ', np_var_int_32.nbytes)          # size of np_var_int_32 in bytes:  4000
print('size of np_var_int_16 in bytes: ', np_var_int_16.nbytes)          # size of np_var_int_16 in bytes:  2000
print()
print('number of elements in np_var_int_32 array: ', np_var_int_32.size) # number of elements in np_var_int_32 array:  1000
print('number of elements in np_var_int_16 array: ', np_var_int_16.size) # number of elements in np_var_int_16 array:  1000

# Output:
# size of existing python list in bytes:  8056
# size of np_var_int_32 in bytes:  4000
# size of np_var_int_16 in bytes:  2000

# number of elements in np_var_int_32 array:  1000
# number of elements in np_var_int_16 array:  1000