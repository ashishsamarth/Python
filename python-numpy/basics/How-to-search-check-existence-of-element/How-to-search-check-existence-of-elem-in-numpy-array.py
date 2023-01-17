# To search / Check existence of an element in Numpy Array
# where() method is used

import numpy as np

np_var=np.array([1,2,3,4,5,6,9,11,-1,1,3,87,8])

# Lets check, if 87 exists in the numpy array
print(np.where(np_var==87))                                                       # (array([11], dtype=int64),)

# To get the indeex of the element, in the numpy array
idx=np.where(np_var==87)
print('The searched element is present in the array at idx position: ', idx[0])   # [11]

# Lets check, if 0 exists in the numpy array
print(np.where(np_var==0))                                                        # (array([], dtype=int64),)
# To get the indeex of the element, in the numpy array
idx=np.where(np_var==0)
print('The searched element is present in the array at idx position: ', idx[0])   # []


# Output
# (array([11], dtype=int64),)
# The searched element is present in the array at idx position:  [11]
# (array([], dtype=int64),)
# The searched element is present in the array at idx position:  []