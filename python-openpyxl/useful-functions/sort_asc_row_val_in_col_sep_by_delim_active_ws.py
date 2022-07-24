from openpyxl.utils import column_index_from_string
# Method to sort values in a given row in an iterative manner
# Arguments to this method are: - Index of column, row number of header, delimiter the values are separated by
# and delimiter value by which the values will be joined by
def sort_asc_row_val_in_col_sep_by_delim_active_ws(self, _header_row_num, _col_name, _delim, _join_by_delim):
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # The Excel columns start with 1, however when iterating, the tuples start with index 0
    for _idx, _val in enumerate(self.get_specific_col_val_by_col_name_in_active_ws(_header_row_num, _col_name),
                                start=1):
        # Bug fix to handle None values in the column
        # Otherwise it will fail during the sorting for split method
        if _val is not None:
            self.my_base_active_ws.cell(row=_idx + _header_row_num,
                                        column=_col_idx).value = _join_by_delim.join(
                sorted([_ for _ in _val.split(_delim)]))
    self.save_wb()