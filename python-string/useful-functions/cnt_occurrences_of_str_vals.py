# Import Collections Package
import collections

# Method to get occurrences of alphabets in string
@staticmethod
# Argument to this method: string
def cnt_occurrences_of_str_vals(_my_string_1):
    return collections.Counter(_my_string_1).values()
