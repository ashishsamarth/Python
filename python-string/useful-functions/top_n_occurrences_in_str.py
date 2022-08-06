# Import Collections Package
import collections

# Method to get top 5 alphabets based on their occurrences in string
@staticmethod
# Arguments to this method: String and Integer
def top_n_occurrences_in_str(_my_string_1, num_of_occurences):
    # We use the 'most_common' method for Counter
    return dict(collections.Counter(_my_string_1).most_common(num_of_occurences))
