# Method to get column values for a given column index
# Arguments to this method are:- Row number for header row & column index
# Note:- Column index starts with 1
def get_specific_col_val_by_col_idx_in_active_ws(self, _header_row_num, _col_idx):
    # Fetch the values from the column index provided
    # Skip the header row
    assert _col_idx >= 1, 'ValueError: Row or column values must be at least 1'
    try:
        return [_col_value[0] for _col_value in self.my_base_active_ws.iter_rows(min_row=_header_row_num + 1,
                                                                                 min_col=_col_idx,
                                                                                 max_col=_col_idx,
                                                                                 values_only=True)]
    except ValueError:
        print('ValueError: Row or column values must be at least 1')
        