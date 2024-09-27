# Convert N dimensional array to 1 dimensional array
import numpy as np

col=6

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
# It creates the fourth rows of the array as [18 19 20 21 22 23], since the start range is 18 and end range is 23
np_mat=np.array([np.arange(col),  np.arange(col, col*2), np.arange(col*2, col*3), np.arange(col*3, col*4)])

print('np_mat :  ', np_mat)
print()

# Get the shape of the array
np_shape=np_mat.shape                                   # output: (4, 6)
np_elem_cnt=np.multiply(np_shape[0], np_shape[1])
print('Countof elements in array: ', np_elem_cnt)       # output: 24
print()

# Now this logic can be applied to array of any size, once you get the np_elem_cnt
np_mat_1D=np.delete(np_mat, np.s_[np_elem_cnt:])
print('np_mat_1D: ', np_mat_1D)

# Output
'''
np_mat :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

Countof elements in array:  24

np_mat_1D:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

'''


# Convert N dimensional array to 1 dimensional array, using ravel()
import numpy as np

col=6

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
# It creates the fourth rows of the array as [18 19 20 21 22 23], since the start range is 18 and end range is 23
np_mat=np.array([np.arange(col),  np.arange(col, col*2), np.arange(col*2, col*3), np.arange(col*3, col*4)])

print('np_mat :  ', np_mat)
print()
np_ravel=np_mat.ravel()
print('1D-Array: ', np_ravel)


# Output
'''
np_mat :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

1D-Array:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
'''