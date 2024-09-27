# To generate array with uniformly distributed values
# use linspace()
# syntax = np.linspace(start_range, end_range, max_limit, dtype=<datatype>)

import numpy as np

np_var=np.linspace(1,5,25,dtype='uint')                         # uint = unsigned integer
print(np_var)

# Output
# [1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 4 4 4 4 4 4 5]