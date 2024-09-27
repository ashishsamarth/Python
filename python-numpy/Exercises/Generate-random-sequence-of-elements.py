# To generate a random sequence of 20 elements, comprising of 15 zeros and 15 ones

import numpy as np

# Utilize the random.randint method
# size keyword is mandatory

np_var=np.random.randint(2, size=30)
print('Randomly Generated array of 0s and 1s: 1st Attempt:- ',np.random.randint(2, size=30))
print('Randomly Generated array of 0s and 1s: 2nd Attempt:- ',np.random.randint(2, size=30))
print('Randomly Generated array of 0s and 1s: 3rd Attempt:- ',np.random.randint(2, size=30))


# Output
# Randomly Generated array of 0s and 1s: 1st Attempt:-  [0 1 0 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 0 1 0 0 1 1 0 1 0]
# Randomly Generated array of 0s and 1s: 2nd Attempt:-  [1 1 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 0 1 1 1 1 0 1 1 1]
# Randomly Generated array of 0s and 1s: 3rd Attempt:-  [1 1 0 1 1 1 0 1 0 1 0 0 1 0 1 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0]