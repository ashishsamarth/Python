# Method to get values for specific row in a given worksheet
# Argument to this method is: - Row number of values to be fetched
def get_specific_row_val_as_str_in_active_ws(self, _val_row_num):
    # Iterate once for all the columns in the active worksheet
    for _col in self.my_base_active_ws.iter_cols(min_col=1, max_col=1):
        # Iterate once for the specific row number in active worksheet
        for _row in self.my_base_active_ws.iter_rows(min_row=_val_row_num, max_row=_val_row_num):
            # Return a string of values
            return ', '.join(map(str, [_cell.value for _cell in _row]))