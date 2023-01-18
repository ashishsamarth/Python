# Iterate over values of matrix:
import numpy as np

np_var=np.random.randint(20,70, size=(3,3))
print('np_var: ', np_var)
print()

# Iterate over values of Matrix - row by row
print('Iterating row by row')
for _ in np_var:
    print('>>>', _)
    
print()

# Iterate over values of Matrix - column by column
print('Iterating column by column')
for _ in np_var.transpose():
    print('>>>', _)


# Output
'''
np_var:  [[65 59 57]
 [28 41 31]
 [45 40 22]]

Iterating row by row
>>> [65 59 57]
>>> [28 41 31]
>>> [45 40 22]

Iterating column by column
>>> [65 28 45]
>>> [59 41 40]
>>> [57 31 22]
'''