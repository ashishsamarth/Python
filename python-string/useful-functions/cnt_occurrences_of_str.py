import collections

# Method to get occurrences of alphabets in string along with string
@staticmethod
# Argument to this method: string
def cnt_occurrences_of_str(_my_string_1):
    # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
    return collections.Counter(_my_string_1)
