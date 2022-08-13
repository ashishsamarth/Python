# Method to check if two strings are anagrams
# Argument to this method: two strings
def are_strs_an_anagram(_inp_str_1, _inp_str_2):
    # Return type is boolean
    return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False