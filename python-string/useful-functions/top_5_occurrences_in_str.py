import collections

# Method to get top 5 alphabets based on their occurrences in string
@staticmethod
# Argument to this method: None
def top_5_occurrences_in_str(_my_string_1):
    # We use the 'most_common' method for Counter
    return dict(collections.Counter(_my_string_1).most_common(5))
