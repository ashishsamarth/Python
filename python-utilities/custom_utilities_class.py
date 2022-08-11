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
    
    # Method to get only lower case letters (a through z)
    @staticmethod
    # Argument to this method: None
    def get_lower_case_alphabets():
        # Return type is a string
        return string.ascii_lowercase