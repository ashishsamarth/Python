# Method to convert a list to a dictionary
# Input:1 - Iterable Sequence
# Input:2 - Starting index position
def convert_list_to_dict(inp_list, starting_idx_position):
    # define an empty dictionary
    output_dict = dict()
    # Enumerate over the input list with a starting counter as zero
    for count, item in enumerate(inp_list,start=starting_idx_position):
        # Assign the counter as key and tuple members as values
        output_dict[count] = item
    return output_dict

print(convert_list_to_dict(inp_list, 5))