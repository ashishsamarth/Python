# Import string module
import string
# Import collections module
import collections
# Import Itertools module
import itertools


# Class definitions should use CamelCase convention based on pep-8 guidelines
class UsefulUtils:

    # Method to get the number of arguments
    # Arguments are passed as a list, separated by comma
    def get_arg_cnt(*_arg):
        # Return type is an integer
        return len(_arg)
 
 