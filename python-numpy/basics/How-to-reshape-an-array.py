# Reshaping an Array

import numpy as np

np_var=np.random.randint(20,70, size=(3,4))
print('np_var: ', np_var)
print()

reshaped_np_var=np_var.reshape(4, 3)
print('reshaped_np_var:', reshaped_np_var)

# Output
'''
np_var:  [[64 49 37 38]
 [49 36 51 22]
 [53 48 39 50]]

reshaped_np_var: [[64 49 37]
 [38 49 36]
 [51 22 53]
 [48 39 50]]
'''