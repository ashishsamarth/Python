# Method to join multiple tuple arguments into one tuple
# Arguments to this method: Multiple tuples as arguments (separated by comma)
# * takes care of the unpacking multiple tuples passed as arguments
def join_tuples(*_tuple_iterables):
    # itertools.chain : joins multiple tuples in to one
    # _tuple_iterables.__class__() : Is a method to enforce that the output result is of same data-type as the input
    # since __class__ will provide the datatype, same as type()
    joined_tuple = _tuple_iterables.__class__(itertools.chain(*_tuple_iterables))
    # Return type is a tuple
    return joined_tuple