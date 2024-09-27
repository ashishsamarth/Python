# Method to get values for specific row in a given worksheet
# Argument to this method is: - Row number of values to be fetched
def get_specific_row_val_as_list_in_active_ws(self, _val_row_num):
    for _col in self.my_base_active_ws.iter_cols():
        # Iterate once for the specific row number in active worksheet
        for _row in self.my_base_active_ws.iter_rows(min_row=_val_row_num, max_row=_val_row_num):
            # Return a list of values
            return [_cell.value for _cell in _row]