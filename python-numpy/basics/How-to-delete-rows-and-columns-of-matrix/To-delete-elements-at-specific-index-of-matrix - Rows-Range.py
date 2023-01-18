# To delete element at specific index of a matrix
# rows are axis=0 and columns are axis=1

import numpy as np

columns=6

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
np_mat=np.array([np.arange(columns),  np.arange(columns, columns*2), np.arange(columns*2, columns*3)])

print('np_mat :  ', np_mat)
print()

# To delete an element at a specific index
# Following example deletes rows at index 2 until 4
np_mat_mod=np.delete(np_mat, np.s_[2:4], axis=0)
print('np_mat_mod :   ', np_mat_mod)

# Output

'''
np_mat :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]]

np_mat_mod :    [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
'''