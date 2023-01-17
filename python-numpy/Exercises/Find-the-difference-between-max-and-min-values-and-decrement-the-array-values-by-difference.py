# Find the difference between largest and smallest values of the array
# Subtract each element of the array with the calculated difference

import numpy as np

np_var=np.random.randint(10, 31, size=15)

np_var_max=np.max(np_var)
np_var_min=np.min(np_var)

np_var_diff=np_var_max-np_var_min

print('np_var: ', np_var)
print('The difference between maximum and mininum values in array is: ', np_var_diff)
final_np_var=np_var-np_var_diff
print('Final numpy array is: ', final_np_var)


# Output
# np_var:  [27 12 26 23 22 25 25 28 12 28 28 26 22 19 12]
# The difference between maximum and mininum values in array is:  16
# Final numpy array is:  [11 -4 10  7  6  9  9 12 -4 12 12 10  6  3 -4]