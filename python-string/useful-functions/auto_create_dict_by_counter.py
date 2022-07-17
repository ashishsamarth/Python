import string
import collections

# Method to get only upper case letters (A through Z)
@staticmethod
# Argument to this method: None
def ret_upr_case_alphabets():
    return string.ascii_uppercase


# Method to create a dictionary dataset automatically
@staticmethod
# Argument to this method: None
def auto_create_dict_by_counter():
    my_string = ret_upr_case_alphabets()
    return dict(collections.Counter(my_string))
