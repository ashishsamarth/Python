# How to generate random sequence of 0s and 1s
# Creation of Numpy single-dimension array
# using random function

import numpy as np
np_var_x=np.random.randint(2, size=20)  # useful for binary data generation
print('np_var_x: ', np_var_x)           # np_var_x:  [1 0 1 1 0 1 0 0 0 1 0 1 0 1 0 1 1 0 1 0]

np_var_y=np.random.randint(2, size=20)  # useful for binary data generation
print('np_var_y: ', np_var_y)           # np_var_y:  [0 0 1 0 0 1 0 0 1 1 1 1 0 0 1 1 0 0 0 1]

# Output:
# np_var_x:  [1 0 1 1 0 1 0 0 0 1 0 1 0 1 0 1 1 0 1 0]
# np_var_y:  [0 0 1 0 0 1 0 0 1 1 1 1 0 0 1 1 0 0 0 1]


# How to generate random sequence of 0s and 1s
# Creation of Numpy single-dimension array
# using random function

import numpy as np
np_var_x=np.random.randint(3,7,size=20)  # useful for random data generation
print('np_var_x: ', np_var_x)            # np_var_x:  [3 3 3 3 3 5 4 4 6 3 6 4 6 4 6 3 4 4 4 5]

np_var_y=np.random.randint(3,7,size=20)  # useful for random data generation
print('np_var_y: ', np_var_y)            # np_var_y:  [4 5 3 6 6 5 6 4 3 5 5 4 4 6 5 4 4 3 4 3]

# Output:
# np_var_x:  [3 3 3 3 3 5 4 4 6 3 6 4 6 4 6 3 4 4 4 5]
# np_var_y:  [4 5 3 6 6 5 6 4 3 5 5 4 4 6 5 4 4 3 4 3]