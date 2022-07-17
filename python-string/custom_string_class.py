# Import String Package

import string
import collections
from xml.etree.ElementTree import TreeBuilder


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomString:

    # Method to only get lower case letters (a through z)
    @staticmethod
    def ret_lwr_case_alphabets():
        return string.ascii_lowercase
    

    # Method to get only upper case letters (A through Z)
    @staticmethod
    def ret_upr_case_alphabets():
        return string.ascii_uppercase
    

    # Method to get both lower case ans upper case letters (a through Z)
    @staticmethod
    def ret_alpha():
        return string.ascii_letters
    

    # Method to get numbers o through 9 as string
    @staticmethod
    def ret_str_0_9():
        return string.digits
    

    # Method to get numbers 0 through 7 as string
    @staticmethod
    def ret_str_0_7():
        return string.octdigits
    

    # Method to get lower case a through f
    @staticmethod
    def ret_str_lwr_case_a_to_f():
        return ''.join(_ for _ in string.hexdigits if _.islower())
    

    # Method to get upper case A through F
    @staticmethod
    def ret_str_upr_case_a_to_f():
        return ''.join(_ for _ in string.hexdigits if _.isupper())
    

    # Method to get special characters
    @staticmethod
    def ret_str_spcl_chars():
        # returns: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return string.punctuation
    

    # Method to reverse the string
    @staticmethod
    # Argument to this method is string
    def ret_str_reversed(_my_string):
        return _my_string[::-1]
    

    # Method to check if a string is a palindrome
    @staticmethod
    def str_is_palindrome(_my_string):
        reversed_string = _my_string[::-1]
        if _my_string == reversed_string:
            return True
        return False


    # Method to check if two strings are anagrams
    @staticmethod
    def strs_are_anagram(_my_string_1, _my_string_2):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return collections.Counter(_my_string_1) == collections.Counter(_my_string_2)
    

    # Method to get occurrences of alphabets in string along with string
    @staticmethod
    def cnt_occurrences_of_str(_my_string_1):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return collections.Counter(_my_string_1)