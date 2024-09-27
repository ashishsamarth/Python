from openpyxl.utils import column_index_from_string
# Method to get column values for a given column letter
# Arguments to this method are:- Row number for header row & column letter
def get_specific_col_val_by_col_letter_in_active_ws(self, _header_row_num, _col_letter):
    assert _col_letter in self.ref_col_letter_name_map(
        _header_row_num).keys(), 'Column Letter Outside Data-Set Range'
    _col_idx = column_index_from_string(_col_letter)
    try:
        return [_col_value[0] for _col_value in self.my_base_active_ws.iter_rows(min_row=_header_row_num + 1,
                                                                                 min_col=_col_idx,
                                                                                 max_col=_col_idx,
                                                                                 values_only=True)]
    except AssertionError:
        print('AssertionError: Column Letter Outside Data-Set Range')