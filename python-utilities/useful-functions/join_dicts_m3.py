# Method to join multiple dictionaries to a single dictionary
# Argument to this method: Multiple Dictionaries as arguments (separated by comma)
# * takes care of the unpacking multiple dictionaries passed as arguments
def join_dicts_m3(*_dicts_iterables):
    # Create an empty dictionary
    merged_dict = {}
    # Iterate over all the dictionaries in the unpacked list of dictionaries
    for _ in _dicts_iterables:
        # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
        merged_dict |= _
    # Return type is a dictionary
    return merged_dict