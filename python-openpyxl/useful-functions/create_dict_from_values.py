# Create a dictionary from Excel cell values
# No arguments to this method
def create_dict_from_values(self):
    # Create an empty dictionary
    _my_dict = dict()
    # get the unique keys (numeric) from the first column of the worksheet
    _my_keys = set([_row[0] for _row in self.my_base_active_ws.values if str(_row[0]).isdigit()])
    # Iterate over the keys and add the values as a list
    for _ in _my_keys:
        # using list comprehension add the values to the key or keys
        _my_dict[_] = [_row[1] for _row in self.my_base_active_ws.values if _row[0] == _]
    return _my_dict