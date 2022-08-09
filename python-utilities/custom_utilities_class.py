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
    
    # Method to join multiple lists into one list
    # Argument to this method: Multiple Lists
    # * takes care of the unpacking multiple lists passed as arguments
    def join_lists(*lists):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*lists))
        # Return type is a list
        return chained_list
    
    # Method to join multiple lists into one list and keep only non-repeating values
    # Argument to this method: Multiple lists
    # * takes care of the unpacking multiple lists passed as arguments
    def merge_lists(*lists):
        # itertools.chain : joins the multiple lists into one
        # set removes the duplicate entries from the list
        # list converts the unique set to a list
        merged_list = list(set(list(itertools.chain(*lists))))
        # Return type is a list
        return merged_list
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m1(*dicts):
        # Using list comprehension to create a new dictionary with keys and values iterated from all input dictionaries
        chained_dict = {k:v for d in dicts for k,v in d.items()}
        # Return type is a dictionary
        return chained_dict