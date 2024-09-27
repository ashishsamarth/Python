from openpyxl.utils import column_index_from_string
# Method to filter rows based on a value present in a specific column of worksheet
# Arguments to this method are: - value used as filter, column idx where filter will be applied
def filter_rows_by_val_in_a_col_in_active_ws(self, _header_row_num, _filter_col_name, _filter_val):
    # Create an empty list to hold values
    # One can always use list comprehension if needed
    returned_val = []
    _filter_col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_filter_col_name])
    # Iterate over the value in the worksheet(column and rows)
    # Note: We are directly iterating over values instead of cell references
    for _main_rec in self.my_base_active_ws.iter_rows(min_row=_header_row_num + 1, values_only=True):
        # If the searched value is found in any cell of the specific column
        # The Excel columns start with 1, however when iterating, the tuples start with index 0
        if str(_filter_val).casefold() == str(_main_rec[_filter_col_idx - 1]).casefold():
            # Append the corresponding row to the empty list
            returned_val.append(_main_rec)
    return returned_val