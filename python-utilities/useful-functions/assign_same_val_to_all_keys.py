# Method to assign same values to provided keys and create a dictionary
# Arguments to this method: _keys as a list of elements, _value as any value
def assign_same_val_to_all_keys(_keys, _value):
    # itertools.repeat : repeats the passed value seamlessly
    # zip : ties the keys and value together together
    my_dict = dict(zip(_keys, itertools.repeat(_value)))
    # Return type is a dictionary
    return my_dict