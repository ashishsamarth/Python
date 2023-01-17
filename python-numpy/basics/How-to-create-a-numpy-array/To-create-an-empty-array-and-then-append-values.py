# How to create and empty NumPy array & elements to it
# arange() :- for creation of single array

import numpy as np

np_var=np.arange(0)
print(np_var)                          # arange(0) returns an empty array

# How to append values to the empty array
np_var=np.append(np_var, 1)
np_var=np.append(np_var, 3)
np_var=np.append(np_var, 5)
np_var=np.append(np_var, 6)
print('np_var: ', np_var)              # np_var: [1 3 5 6]

# Output
# []
# np_var:  [1 3 5 6]