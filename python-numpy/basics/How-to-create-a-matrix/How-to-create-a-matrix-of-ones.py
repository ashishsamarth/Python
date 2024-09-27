# To Create a Matrix with specific values

import numpy as np

np_mat=np.ones((5,2))
print(np_mat)

# Output  (The output is float datatype)

'''
[[1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]]
'''

# To Create a Matrix with specific values with specific datatype

import numpy as np

np_mat=np.ones((5,2), dtype=int)
print(np_mat)

# Output (The output is int datatype)
'''
[[1 1]
 [1 1]
 [1 1]
 [1 1]
 [1 1]]
'''