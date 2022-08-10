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
    # Arguments to this method: _keys as a list of elements, _value as any value
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
        # Using list comprehension to create a new dictionary with keys and values iterated from all the dictionaries in the unpacked list of dictionaries
        chained_dict = {k:v for d in dicts for k,v in d.items()}
        # Return type is a dictionary
        return chained_dict
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m2(*dicts):
        # Create an empty dictionary
        chained_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in dicts:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            chained_dict.update(_)
        # Return type is a dictionary
        return chained_dict
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m3(*dicts):
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in dicts:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Return type is a dictionary
        return merged_dict
    
    # Method to join multiple dictionaries to a single dictionary and sort by keys in ascending order
    # Argument to this method: Multiple Dictionaries
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_sort_by_keys_asc(*dicts):
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in dicts:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Sort the updated dictionary based on keys in ascending order
        # usage of sorted method: sorted(iterable, key)
        # for sorting key, I am using the anonymous lambda function and item[0] refers to the dictionary keys
        sorted_dict = dict(sorted(merged_dict.items(), key=lambda item:item[0]))
        # Return type is a dictionary
        return sorted_dict

    # Method to join multiple dictionaries to a single dictionary and sort by keys in ascending order
    # Argument to this method: Multiple Dictionaries
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_sort_by_vals_asc(*dicts):
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in dicts:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Sort the updated dictionary based on values in ascending order
        # usage of sorted method: sorted(iterable, key)
        # for sorting key, I am using the anonymous lambda function and item[-1] refers to the dictionary values
        sorted_dict = dict(sorted(merged_dict.items(), key=lambda item:item[-1]))
        # Return type is a dictionary
        return sorted_dict

    def join_dicts_sort_by_keys_desc(*dicts):
        