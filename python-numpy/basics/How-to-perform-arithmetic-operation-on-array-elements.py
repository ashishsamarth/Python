# Perform Arithmetic operation on each element of an array

import numpy as np

np_var=np.array([1000, 2000, 3000, 4000, 5000])
np_var_increment=np_var+200                      # Increment array values by a number
np_var_decrement=np_var-100                      # Decrement array values by a number
np_var_multiply=np_var*2                         # Multiply array values by a number
np_var_divide=np_var/5                           # Divide array values by a number

np_var_complex_op=(((np_var+200)*2)/6.5)         # some equation on array values by a number

print('np_var_increment: ', np_var_increment)
print('np_var_decrement: ', np_var_decrement)
print('np_var_multiply: ', np_var_multiply)
print('np_var_divide: ', np_var_divide)
print('np_var_complex_op: ', np_var_complex_op)


# Output
# np_var_increment:  [1200 2200 3200 4200 5200]
# np_var_decrement:  [ 900 1900 2900 3900 4900]
# np_var_multiply:  [ 2000  4000  6000  8000 10000]
# np_var_divide:  [ 200.  400.  600.  800. 1000.]
# np_var_complex_op:  [ 369.23076923  676.92307692  984.61538462 1292.30769231 1600.]