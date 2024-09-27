# To remove duplicates from a NumPy array
# To get only uniques from a Numpy array

import numpy as np

np_var=np.array([1,2,3,4,5,6,9,11,-1,1,3,87,8])
print('Original Order of elements in the array: ', np_var)

print('Unique Elements in the Numpy array are: ', np.unique(np_var))

# The challenge with np.unique is - It will sort the elements automatically

# If you would like to retain the order of the elements occurence, we have to utilize its index
np_var_orig_order, idx=np.unique(np_var, return_index=True)
print('Unique Elements in the Numpy array with original order: ', np_var_orig_order[np.argsort(idx)])


# Output:
# Original Order of elements in the array:  [ 1  2  3  4  5  6  9 11 -1  1  3 87  8]
# Unique Elements in the Numpy array are:  [-1  1  2  3  4  5  6  8  9 11 87]   
# Unique Elements in the Numpy array with original order:  [ 1  2  3  4  5  6  9 11 -1 87  8]