# Copying data from a matrix
import numpy as np

col=6

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
# It creates the fourth rows of the array as [18 19 20 21 22 23], since the start range is 18 and end range is 23
np_mat_x=np.array([np.arange(col),  np.arange(col, col*2), np.arange(col*2, col*3), np.arange(col*3, col*4)])

print('np_mat_x :  ', np_mat_x)
print()

# Shallow Copy
print('#####---Example of Shallow Copy---####')
np_mat_y = np_mat_x
print('np_mat_y :  ', np_mat_y)
print()

# Changing one particular value in np_mat_x
np_mat_x[3,0]=85
print('np_mat_x :  ', np_mat_x)
print()
print('The value of np_mat_y was also modified, even when np_mat_x was changed, and we did not update the value of np_mat_y')
print('This behavior is due to shallow copy')
print()
print('np_mat_y :  ', np_mat_y)

print('-----------------------------------------------------')
print('-----------------------------------------------------')

col=6

# How to understand the following line
# It creates the first row of the array as [0 1 2 3 4 5], since the array range end is 6
# It creates the second row of the array as [6 7 8 9 10 11], since the start range is 6 and end range is 12
# It creates the third rows of the array as [12 13 14 15 16 17], since the start range is 12 and end range is 18
# It creates the fourth rows of the array as [18 19 20 21 22 23], since the start range is 18 and end range is 23
np_mat_a=np.array([np.arange(col),  np.arange(col, col*2), np.arange(col*2, col*3), np.arange(col*3, col*4)])

print('np_mat_a :  ', np_mat_a)
print()
# Deep Copy
print('#####---Example of Deep Copy---####')

np.copyto(np_mat_b, np_mat_a)
print('np_mat_b :  ', np_mat_b)
print()

# Changing one particular value in np_mat_x
np_mat_a[3,0]=85
print('np_mat_a :  ', np_mat_a)
print()
print('The value of np_mat_y was not modified, even when np_mat_x was changed')
print('This behavior is due to deep copy')
print()
print('np_mat_b :  ', np_mat_b)

# Output:
'''

np_mat_x :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

#####---Example of Shallow Copy---####
np_mat_y :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

np_mat_x :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [85 19 20 21 22 23]]

The value of np_mat_y was also modified, even when np_mat_x was changed, and we did not update the value of np_mat_y
This behavior is due to shallow copy

np_mat_y :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [85 19 20 21 22 23]]
-----------------------------------------------------
-----------------------------------------------------
np_mat_a :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

#####---Example of Deep Copy---####
np_mat_b :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

np_mat_a :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [85 19 20 21 22 23]]

The value of np_mat_y was not modified, even when np_mat_x was changed
This behavior is due to deep copy

np_mat_b :   [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

'''