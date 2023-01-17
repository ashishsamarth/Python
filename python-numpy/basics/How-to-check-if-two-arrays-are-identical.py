# Check if two arrays are identifical
# identical = Same number of elements, and elements at the same indexes of both arrays

import numpy as np

# Define three arrays
np_var_1=np.array([1,2,3,4,5,6])
np_var_2=np.array([1,2,3,4,5,6])
np_var_3=np.array([1,2,3,5,4,6])

print('Are np_var_1 and np_var_2 identical: ', np.array_equal(np_var_1, np_var_2))   # True
print('Are np_var_2 and np_var_3 identical: ', np.array_equal(np_var_2, np_var_3))   # False
print('Are np_var_1 and np_var_3 identical: ', np.array_equal(np_var_1, np_var_3))   # False

# Output
# Are np_var_1 and np_var_2 identical:  True
# Are np_var_2 and np_var_3 identical:  False
# Are np_var_1 and np_var_3 identical:  False