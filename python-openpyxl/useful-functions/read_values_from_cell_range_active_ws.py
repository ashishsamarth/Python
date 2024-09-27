# Method to read values from a cell range
# Arguments to this method are:- Row number for header row, Start range and Ending range
def read_values_from_cell_range_active_ws(self, _header_row_num, _start_range, _end_range):
    # Split start range to determine 'Column Letter' and Row index
    _start_rng_col = ''.join([_ for _ in _start_range if _.isalpha()])
    _start_rng_row = ''.join([_ for _ in _start_range if _.isdigit()])
    _end_rng_col = ''.join([_ for _ in _end_range if _.isalpha()])
    _end_rng_row = ''.join([_ for _ in _end_range if _.isdigit()])
    # Create an empty list to hold iterated values
    _my_val = []
    # Iterate over the values (row-wise) of the active worksheet
    # minimum row - Is the row number from the start range
    # maximum row - Is the row number from the end range
    # minimum column - Is the column index fetched from 'ref_col_letter_idx_map' method using column letter
    # maximum column - Is the column index fetched from 'ref_col_letter_idx_map' method using column letter + 1
    # 1 is added to maximum column to make the last column inclusive for result return
    for _val in self.my_base_active_ws.iter_rows(values_only=True,
                                                 min_row=int(_start_rng_row),
                                                 min_col=int(
                                                     self.ref_col_letter_idx_map(_header_row_num)[_start_rng_col]),
                                                 max_row=int(_end_rng_row),
                                                 max_col=int(self.ref_col_letter_idx_map(_header_row_num)[
                                                                 _end_rng_col] + 1)):
        _my_val.append(_val)
    return _my_val