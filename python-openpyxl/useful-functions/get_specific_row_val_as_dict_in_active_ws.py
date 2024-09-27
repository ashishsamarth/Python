# Method to get values for specific row in a given worksheet
# Arguments to this method are: - Row number of values to be fetched and Row number of header row
def get_specific_row_val_as_dict_in_active_ws(self, _header_row_num, _val_row_num):
    # Iterate once for all the columns in the active worksheet
    _col_keys = [_ for _ in self.ref_col_name_idx_map(_header_row_num).keys()]
    # Create an empty list
    _row_values = []
    # Iterate once for all the columns in the active worksheet
    for _col in self.my_base_active_ws.iter_cols():
        # Iterate once for the specific row number in active worksheet
        for _row in self.my_base_active_ws.iter_rows(min_row=_val_row_num, max_row=_val_row_num):
            # for each cell in the row
            for _cell in _row:
                # Return a list of values
                _row_values.append(_cell.value)
        # Using the  _col_keys  and _row_values create a dictionary
        _result_set = dict(zip(_col_keys, _row_values))
        # Return a dictionary of values
        return _result_set