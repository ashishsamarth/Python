# Import String Package
import string

# Method to get lower case a through f
@staticmethod
# Argument to this method: None
def ret_str_lwr_case_a_to_f():
    return ''.join(_ for _ in string.hexdigits if _.islower())
