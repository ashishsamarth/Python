# Method to convert a tuple to a dictionary
# Input:1 - Iterable Sequence
# Input:2 - Starting Counter position
def convert_tuple_to_dict(inp_tuple, starting_idx_position):
    # define an empty dictionary
    output_dict = dict()
    # Enumerate over the input set with a starting counter as provided by user
    for count, item in enumerate(inp_tuple,start=starting_idx_position):
        # Assign the counter as key and tuple members as values
        output_dict[count] = item
    return output_dict