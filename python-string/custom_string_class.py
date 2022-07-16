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
    