# Matrix Dot Product

import numpy as np

np_var_x=np.random.randint(1,5, size=(3,4))
np_var_y=np.random.randint(1,5, size=(4,3))

print('np_var_x: ', np_var_x)
print()
print('np_var_y: ', np_var_y)

np_var_z=np.dot(np_var_x, np_var_y)

# How to dot product is calculated
# First Row: First-element (18)     :(1*2 + 4*2 + 2*3 + 1*2)
# First Row: second-element (26)    :(1*3 + 4*3 + 2*4 + 1*3)
# First Row: Third-element (26)     :(1*4 + 4*3 + 2*4 + 1*2)

# Second Row: First-element (23)    :(1*2 + 4*2 + 3*3 + 2*2) 
# Second Row: second-element (33)   :(1*3 + 4*3 + 3*4 + 2*3)
# Second Row: Third-element (32)    :(1*4 + 4*3 + 3*4 + 2*2) 

# Third Row: First-element (23)     : (2*2 + 4*2 + 1*3 + 4*2) 	
# Third Row: second-element (34)    : (2*3 + 4*3 + 1*4 + 4*3)
# Third Row: Third-element (32)     : (2*4 + 4*3 + 1*4 + 4*2)

print()
print('np_var_z: ', np_var_z)

# output

'''
np_var_x:  [[1 4 2 1]
 [1 4 3 2]
 [2 4 1 4]]

np_var_y:  [[2 3 4]
 [2 3 3]
 [3 4 4]
 [2 3 2]]

np_var_z:  [[18 26 26]
 [23 33 32]
 [23 34 32]]

'''