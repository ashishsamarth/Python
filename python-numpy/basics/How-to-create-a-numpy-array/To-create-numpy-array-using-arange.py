# How to create an NumPy Array
# Creation of NumPy single-dimension array
# arange() :- for creation of single array

import numpy as np
np_var=np.arange(9)         # Creates an arary [0 1 2 3 4 5 6 7 8]
print(np_var)
print(type(np_var))         # <class'numpy.ndarray'> : ndarray = n-dimensional array


# output:
# [0 1 2 3 4 5 6 7 8]
# <class 'numpy.ndarray'>


np_var1=np.arange(5)  
print('np_var1: ', np_var1)           # np_var1: [0 1 2 3 4]

np_var2=np.arange(1, 2.5, .1)         # Creates an array with increments of 0.1 between ranges
print('np_var2: ', np_var2)           # np_var2: [1. 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. 2.1 2.2 2.3 2.4]

np_var3=np.arange(20, 30)             # Creates an array with increments of 1 between ranges
print('np_var3: ', np_var3)           # np_var3: [20 21 22 23 24 25 26 27 28 29]

np_var4=np.arange(20, 40, 2)          # Creates an array with increments of 2 between ranges
print('np_var4: ', np_var4)           # np_var4: [20 22 24 26 28 30 32 34 36 38]

np_var5=np.arange(20, 30, 2, float)   # Creates an array with increments of 2 between ranges
print('np_var5: ', np_var5)           # np_var5: [20. 22. 24. 26. 28.]

# Output
# np_var1:  [0 1 2 3 4]
# np_var2:  [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.  2.1 2.2 2.3 2.4]
# np_var3:  [20 21 22 23 24 25 26 27 28 29]
# np_var4:  [20 22 24 26 28 30 32 34 36 38]
# np_var5:  [20. 22. 24. 26. 28.]