# Method to assign same values to provided keys and create a dictionary
# Arguments to this method: _keys as a list of elements, _value as any value
def assign_same_val_to_all_keys(*_keys, _value):
    # itertools.repeat : repeats the passed value seamlessly
    # zip : ties the keys and value together together
    # itertools.chain(*_keys) : Joins all lists to form a single list
    # Return type is a dictionary
    return dict(zip(itertools.chain(*_keys), itertools.repeat(_value)))