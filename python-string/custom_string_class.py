# Import String Package

import string
import collections


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
    