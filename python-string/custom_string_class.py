# Import string package
# Import collections package

import string
import collections


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomString:

    # Method to only get lower case letters (a through z)
    @staticmethod
    # Argument to this method: None
    def ret_lwr_case_alphabets():
        return string.ascii_lowercase
    

    # Method to get only upper case letters (A through Z)
    @staticmethod
    # Argument to this method: None
    def ret_upr_case_alphabets():
        return string.ascii_uppercase
    

    # Method to get both lower case ans upper case letters (a through Z)
    @staticmethod
    # Argument to this method: None
    def ret_alpha():
        return string.ascii_letters
    

    # Method to get numbers o through 9 as string
    @staticmethod
    # Argument to this method: None
    def ret_str_0_9():
        return string.digits
    

    # Method to get numbers 0 through 7 as string
    @staticmethod
    # Argument to this method: None
    def ret_str_0_7():
        return string.octdigits
    

    # Method to get lower case a through f
    @staticmethod
    # Argument to this method: None
    def ret_str_lwr_case_a_to_f():
        return ''.join(_ for _ in string.hexdigits if _.islower())
    

    # Method to get upper case A through F
    @staticmethod
    # Argument to this method: None
    def ret_str_upr_case_a_to_f():
        return ''.join(_ for _ in string.hexdigits if _.isupper())
    

    # Method to get special characters
    @staticmethod
    # Argument to this method: None
    def ret_str_spcl_chars():
        # returns: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return string.punctuation
    

    # Method to reverse the string
    @staticmethod
    # Argument to this method: string
    def ret_str_reversed(_my_string):
        return _my_string[::-1]
    

    # Method to check if a string is a palindrome
    @staticmethod
    # Argument to this method: string
    def str_is_palindrome(_my_string):
        reversed_string = _my_string[::-1]
        if _my_string == reversed_string:
            return True
        return False


    # Method to check if two strings are anagrams
    @staticmethod
    # Argument to this method: string
    def strs_are_anagram(_my_string_1, _my_string_2):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return collections.Counter(_my_string_1) == collections.Counter(_my_string_2)
    

    # Method to get occurrences of alphabets in string along with string
    @staticmethod
    # Argument to this method: string
    def cnt_occurrences_of_str(_my_string_1):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return collections.Counter(_my_string_1)

    # Method to get occurrences of alphabets in string
    # Sort the result dictionary by key or value
    # Order the dictionary in asc or desc
    @staticmethod
    # Arguments to this method are: string, sorting key and sorting type
    def cnt_occurrences_of_str_ordered_rslt(_my_string_1, _sort_key, _sort_type):
        result_set = collections.Counter(_my_string_1)
        if _sort_key == 'k':
            return collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_type))
        elif _sort_key == 'v':
            return collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_type))
    

    # Method to get unique alphabets from string
    @staticmethod
    # Argument to this method: string
    def cnt_occurrences_of_str_keys(_my_string_1):
        return collections.Counter(_my_string_1).keys()
    

    # Method to get occurrences of alphabets in string
    @staticmethod
    # Argument to this method: string
    def cnt_occurrences_of_str_vals(_my_string_1):
        return collections.Counter(_my_string_1).values()
    

    # Method to create a dictionary dataset automatically
    @staticmethod
    # Argument to this method: None
    def auto_create_dict_by_counter():
        my_string = CustomString.ret_upr_case_alphabets()
        return dict(collections.Counter(my_string))
    

    # Method to get top 5 alphabets based on their occurrences in string
    @staticmethod
    # Argument to this method: string
    def top_5_occurrences_in_str(_my_string_1):
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_my_string_1).most_common(5))
    

    # Method to check if given string is empty or not
    @staticmethod
    # Argument to this method: string
    def chk_if_string_empty(_my_string: str):
        if not _my_string:
            return f'Given String is empty'
        return f'Given String is not empty'
