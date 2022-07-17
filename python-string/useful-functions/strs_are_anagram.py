# Import collections Package
import collections

# Method to check if two strings are anagrams
@staticmethod
# Arguments to this method: strings
def strs_are_anagram(_my_string_1, _my_string_2):
    # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
    return collections.Counter(_my_string_1) == collections.Counter(_my_string_2)
