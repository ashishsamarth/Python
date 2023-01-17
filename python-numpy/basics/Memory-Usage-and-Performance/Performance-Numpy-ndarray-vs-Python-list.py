# Memory Usage and Performance
# NumPy array vs Python List (Performance)
# Scenario: Addition of elements in a list

import numpy as np
import time

_my_lst_size=10000

# create a list based on the range(size) variable
_my_lst=list(range(_my_lst_size))

# Capture start time of operation
_start_time_1=time.perf_counter()
_my_lst_sum=sum(_my_lst)                                # Addition of elements in the python list
# Identify execution time of the operation
print(f"Time Taken by python sum operation of python list is {(time.perf_counter() - _start_time_1)} seconds")

# create a numpy array from the existing python list
np_var=np.array(_my_lst)

# Capture start time of operation
_start_time_2=time.perf_counter()
# Calling python sum function on numpy array
np_var_sum=np_var.sum()
# Identify execution time of the operation
print(f"Time Taken by python sum operation of numpy array is {(time.perf_counter() - _start_time_2)} seconds")

# Capture start time of operation
_start_time_3=time.perf_counter()
# Calling numpy sum function on numpy array
np_var_sum_np=np.sum(np_var)
# Identify execution time of the operation
print(f"Time Taken by numpy sum operation of numpy array is {(time.perf_counter() - _start_time_3)} seconds")
print()


# Output
# Time Taken by python sum operation of python list is 0.00040949999947770266 seconds
# Time Taken by python sum operation of numpy array is 0.0003065999999307678 seconds
# Time Taken by numpy sum operation of numpy array is 0.00026840000009542564 seconds