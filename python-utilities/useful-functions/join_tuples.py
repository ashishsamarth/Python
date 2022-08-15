# Method to join multiple tuple arguments into one tuple
# Arguments to this method: Multiple tuples as arguments (separated by comma)
# * takes care of the unpacking multiple tuples passed as arguments
def join_tuples(*_tuple_iterables):
    # itertools.chain : joins multiple tuples in to one
    joined_tuple = tuple(itertools.chain(*_tuple_iterables))
    # Return type is a tuple
    return joined_tuple