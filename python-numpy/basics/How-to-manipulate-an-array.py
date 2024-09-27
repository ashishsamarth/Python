# Array Manipulation

import numpy as np

# Create an array of shape(4,5) having all values as 10
# using the full() method

np_var = np.full((4,5), 10)
print('np_var: ', np_var)
print()

# update all values in the array to be 0
# Three dots are mandatory syntax
np_var[...]=0
print('np_var_with_all_zeros: ', np_var)
print()

# update the column at index=1 to have value as 5 on all rows
np_var[..., 1]=5
print('np_var_all_5s_on_column=2: ', np_var)
print()

# update the column at index=3 to have value as 7 on all rows
np_var[..., 3]=7
print('np_var_all_7s_on_column=4: ', np_var)
print()

# update the row at index=2 to have value as 9 on all colums
np_var[2, ...]=9
print('np_var_all_9s_on_row=3: ', np_var)
print()

# update the column at index=2 and row at index=1 with a value of 85
np_var[1,2]=85
print('np_var_specific_idx: ', np_var)
print()


# Output

'''
np_var:  [[10 10 10 10 10]
 [10 10 10 10 10]
 [10 10 10 10 10]
 [10 10 10 10 10]]

np_var_with_all_zeros:  [[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]

np_var_all_5s_on_column=2:  [[0 5 0 0 0]
 [0 5 0 0 0]
 [0 5 0 0 0]
 [0 5 0 0 0]]

np_var_all_7s_on_column=4:  [[0 5 0 7 0]
 [0 5 0 7 0]
 [0 5 0 7 0]
 [0 5 0 7 0]]

np_var_all_9s_on_row=3:  [[0 5 0 7 0]
 [0 5 0 7 0]
 [9 9 9 9 9]
 [0 5 0 7 0]]

np_var_specific_idx:  [[ 0  5  0  7  0]
 [ 0  5 85  7  0]
 [ 9  9  9  9  9]
 [ 0  5  0  7  0]]

'''