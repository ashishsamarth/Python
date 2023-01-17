# Sort a NumPy Array

import numpy as np

np_var=np.array([1,2,3,4,5,6,9,11,-1])

# Default behavior : Sort Ascending
print('sorted ascending np_var_1: ', np.sort(np_var))     # sorted ascending np_var_1:  [-1  1  2  3  4  5  6  9 11]
# Sorted: Descending
print('sorted descending np_var_1: ', -np.sort(-np_var))  # sorted descending np_var_1:  [11  9  6  5  4  3  2  1 -1]
print()

# Numpy Array with Integers and Floats
np_var=np.array([3,4,6,9,-1, 2.5])
# Default behavior : Sort Ascending
print('sorted ascending np_var_1: ', np.sort(np_var))     # sorted ascending np_var_1:  [-1.   2.5  3.   4.   6.   9. ]
# Sorted: Descending
print('sorted descending np_var_1: ', -np.sort(-np_var))  # sorted descending np_var_1:  [9.   6.   4.   3.   2.5 -1. ]
print()

# Output
# sorted ascending np_var_1:  [-1  1  2  3  4  5  6  9 11]
# sorted descending np_var_1:  [11  9  6  5  4  3  2  1 -1]
# sorted ascending np_var_1:  [-1.   2.5  3.   4.   6.   9. ]
# sorted descending np_var_1:  [ 9.   6.   4.   3.   2.5 -1. ]