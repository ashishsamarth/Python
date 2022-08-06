# Import Collections Module
import collections

# Method to get unique alphabets from string
@staticmethod
# Argument to this method: string
def cnt_occurrences_of_str_keys(_my_string_1):
    return collections.Counter(_my_string_1).keys()
