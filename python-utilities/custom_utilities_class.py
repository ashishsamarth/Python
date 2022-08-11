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