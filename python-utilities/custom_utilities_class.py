# import Itertools module
import itertools


# Define a new class
class UsefulUtils:

    # Method to get the number of arguments
    # Arguments are passed as a list
    def get_arg_count(*_arg):
        # Return type is an integer
        return len(_arg)