# Import string module
import string
# Import collections module
import collections
# Import Itertools module
import itertools


# Class definitions should use CamelCase convention based on pep-8 guidelines
class UsefulUtils:

    # Method to check if two strings are anagrams
    # Argument to this method: two strings
    def are_strs_an_anagram(_inp_str_1: str, _inp_str_2: str):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False
    
    # Method to get occurrences of alphabets in string along with string
    # Argument to this method: string
    def cnt_elem_occurrences_in_str(_inp_str: str):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return dict(collections.Counter(_inp_str))

    # Method to get occurrences of alphabets in string
    # Sort the result dictionary by key or value
    # Order the dictionary in asc or desc based on _sort_reversal
    # Valid values for _sort_reversal are True / False
    # Valid values for _sort_key are key / value
    # Arguments to this method are: string, sorting key and sorting type
    def cnt_elem_occurrences_in_str_ordered_rslt(_inp_str:str, _sort_key='key', _sort_reversal=False):
        # collections.Counter will create a dictionary structure and get the count of each element of the string
        # element is the key and count is the value of that key
        result_set = collections.Counter(_inp_str)
        # Following if statement is triggered when user wants to sort the result by key
        if _sort_key == 'key':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_reversal)))
        # Following elif statement is triggered when user wants to sort the result by value of the key
        elif _sort_key == 'value':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_reversal)))    