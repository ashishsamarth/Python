# Exercise 1:- Create an array of 15 elements with random values in the range 10 to 30 (both inclusive)
import numpy as np

# utilize the random.randint()
# set up the range for 10, 31(so that 30 is included too)
# size is an important parameter
np_var=np.random.randint(10, 31, size=15)
print(np_var)

# Output
# [18 26 20 14 28 29 26 20 21 16 15 22 30 16 24]
