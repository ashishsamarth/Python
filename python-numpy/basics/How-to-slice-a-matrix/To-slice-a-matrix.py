# Slice a matrix

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

# Slice top-left 3 rows and 3 columns
np_mat_3r_3c = np_mat_x[0:3, 0:3]
print('np_mat_3r_3c: ', np_mat_3r_3c)
print()

# Slice top-left 2 rows and 3 columns
np_mat_2r_3c = np_mat_x[0:2, 0:3]
print('np_mat_2r_3c: ', np_mat_2r_3c)
print()

# Slice top 2 rows
np_mat_2r_t = np_mat_x[0:2]
print('np_mat_2r_t: ', np_mat_2r_t)
print()

# Slice bottom 2 rows
np_mat_2r_b = np_mat_x[2:]
print('np_mat_2r_b: ', np_mat_2r_b)
print()

# Slice last row
np_mat_last_r = np_mat_x[3:]
print('np_mat_last_r: ', np_mat_last_r)
print()

# Output

'''
np_mat_x:  [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

np_mat_3r_3c:  [[ 0  1  2]
 [ 4  5  6]
 [ 8  9 10]]

np_mat_2r_3c:  [[0 1 2]
 [4 5 6]]

np_mat_2r_t:  [[0 1 2 3]
 [4 5 6 7]]

np_mat_2r_b:  [[ 8  9 10 11]
 [12 13 14 15]]

np_mat_last_r:  [[12 13 14 15]]

'''