# import Itertools module
import itertools


# Define a new class
class UsefulUtils:

    # Method to get the number of arguments
    # Arguments are passed as a list
    def get_arg_count(*_arg):
        # Return type is an integer
        return len(_arg)
    
    # Method to assign same values to provided keys
    # Arguments to this method: _keys as a list, _value as any value
    def assign_same_val_to_keys(_keys, _value):
        # itertools.repeat : repeats the passed value seamlessly
        # zip : ties the keys and value together together
        my_dict = dict(zip(_keys, itertools.repeat(_value)))
        # Return type is a dictionary
        return my_dict