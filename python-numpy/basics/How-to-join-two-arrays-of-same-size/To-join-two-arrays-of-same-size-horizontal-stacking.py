# Join two arrays
# Their are two methods, one is horizontal stacking and another is vertical stacking

import numpy as np

col=4

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
# It creates the fourth rows of the array as [18 19 20 21 22 23], since the start range is 18 and end range is 23
np_mat_x=np.array([np.arange(col),  np.arange(col, col*2), np.arange(col*2, col*3), np.arange(col*3, col*4)])

print('np_mat_x: ', np_mat_x)
print()
np_mat_y=np.diag((1,2,3,4))
print('np_mat_y: ', np_mat_y)
print()

# joining both matrix, horizontally
horizontal_matrix=np.hstack((np_mat_x, np_mat_y))
print('horizontal_matrix: ', horizontal_matrix)
print()

# Outpt:

'''
np_mat_x:  [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

np_mat_y:  [[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]

horizontal_matrix:  [[ 0  1  2  3  1  0  0  0]
 [ 4  5  6  7  0  2  0  0]
 [ 8  9 10 11  0  0  3  0]
 [12 13 14 15  0  0  0  4]]
'''