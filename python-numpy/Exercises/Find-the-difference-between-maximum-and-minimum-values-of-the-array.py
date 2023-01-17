# Find the difference between largest and smallest values of the array
import numpy as np

np_var=np.random.randint(10, 31, size=15)

np_var_max=np.max(np_var)
np_var_min=np.min(np_var)

np_var_diff=np_var_max-np_var_min

print('np_var: ', np_var)
print('The difference between maximum and mininum values in array is: ', np_var_diff)

# Output
# np_var:  [17 17 10 30 23 28 29 13 21 10 21 12 19 14 22]
# The difference between maximum and mininum values in array is:  20