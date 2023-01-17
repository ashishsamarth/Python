# How to delete elements from a NumPy array

import numpy as np

np_var_orig=np.arange(10,30,2)                      # Create a numpy array

# To delete element at specific index
np_var_mod=np.delete(np_var_orig, 3)                # Delete the element at the 3rd index starting from zero

print('np_var_orig: ', np_var_orig)                 # np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
print('np_var_mod: ', np_var_mod)                   # np_var_mod:  [10 12 14 18 20 22 24 26 28]

# To delete element(s) at specific indices
np_var_mod2=np.delete(np_var_orig, [3,4,7,8])       # Delete the elements at specific indices
print('np_var_orig: ', np_var_orig)                 # np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
print('np_var_mod2: ', np_var_mod2)                 # np_var_mod2:  [10 12 14 20 22 28]

# To delete element(s) in the range
np_var_mod3=np.delete(np_var_orig, np.s_[3:8])      # Delete the elements in the range (np.s_ : generates slice object)
print('np_var_orig: ', np_var_orig)                 # np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
print('np_var_mod3: ', np_var_mod3)                 # np_var_mod3:  [10 12 14 26 28]


# Output
# np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
# np_var_mod:  [10 12 14 18 20 22 24 26 28]
# np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
# np_var_mod2:  [10 12 14 20 22 28]
# np_var_orig:  [10 12 14 16 18 20 22 24 26 28]
# np_var_mod3:  [10 12 14 26 28]