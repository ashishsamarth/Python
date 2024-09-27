# Method to filter a row based on a value present in any column of worksheet
# Argument to this method is:- value to be used as filter
def filter_rows_by_val_in_any_col_in_active_ws(self, _header_row_num, _filter_val):
    # Create an empty list to hold values
    # One can always use list comprehension if needed
    returned_val = []
    # Iterate over the value in the worksheet(column and rows)
    # Note: We are directly iterating over values instead of cell references
    for _main_rec in self.my_base_active_ws.iter_rows(min_row=_header_row_num + 1, values_only=True):
        # If the searched value is found in any of the cells of any column
        if str(_filter_val).casefold() in str(_main_rec).casefold():
            # Append the corresponding row to the empty list
            returned_val.append(_main_rec)
    return returned_val