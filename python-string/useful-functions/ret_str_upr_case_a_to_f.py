# Import String Package
import string

# Method to get upper case A through F
@staticmethod
# Argument to this method: None
def ret_str_upr_case_a_to_f():
    return ''.join(_ for _ in string.hexdigits if _.isupper())
