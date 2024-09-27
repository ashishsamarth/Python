# To keep columns at specific ranges of column range
# rows are axis=0 and columns are axis=1

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

# To Keep only first column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_1st_column=np.delete(np_mat, np.s_[1:], axis=1)
print('np_mat_keep_1st_column: ', np_mat_keep_1st_column)

print()

# To Keep only second column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_2nd_column=np.delete((np.delete(np_mat, np.s_[2:], axis=1)), np.s_[0:1], axis=1)
print('np_mat_keep_2nd_column: ', np_mat_keep_2nd_column)

print()

# To Keep only third column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_3rd_column=np.delete((np.delete(np_mat, np.s_[3:], axis=1)), np.s_[0:2], axis=1)
print('np_mat_keep_3rd_column: ', np_mat_keep_3rd_column)

print()

# To Keep only fourth column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_4rth_column=np.delete((np.delete(np_mat, np.s_[4:], axis=1)), np.s_[0:3], axis=1)
print('np_mat_keep_4rth_column: ', np_mat_keep_4rth_column)

print()

# To Keep only fifth column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_5th_column=np.delete((np.delete(np_mat, np.s_[4:], axis=1)), np.s_[0:3], axis=1)
print('np_mat_keep_5th_column: ', np_mat_keep_5th_column)

print()

# To Keep only sixth column of the matrix
# Note: np.s_ (slice) is used here which can work with the ranges as well
np_mat_keep_6th_column=np.delete((np.delete(np_mat, np.s_[4:], axis=1)), np.s_[0:3], axis=1)
print('np_mat_keep_6th_column: ', np_mat_keep_6th_column)

print()

# Output
'''
np_mat :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

np_mat_keep_1st_column:  [[ 0]
 [ 6]
 [12]
 [18]]

np_mat_keep_2nd_column:  [[ 1]
 [ 7]
 [13]
 [19]]

np_mat_keep_3rd_column:  [[ 2]
 [ 8]
 [14]
 [20]]

np_mat_keep_4rth_column:  [[ 3]
 [ 9]
 [15]
 [21]]

np_mat_keep_5th_column:  [[ 3]
 [ 9]
 [15]
 [21]]

np_mat_keep_6th_column:  [[ 3]
 [ 9]
 [15]
 [21]]

'''
