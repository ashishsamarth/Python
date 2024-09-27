from openpyxl.utils import column_index_from_string
# Method to get row indexes of searched values in a specific column with near match condition
# Arguments to this method are:- Row number for header row, Column name & Search value
def get_row_idx_lst_based_on_search_val_specific_col_near_match(self, _header_row_num, _col_name, _search_val):
    # Fetch the column index from column name using 'ref_col_name_letter_map' method
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # Get the list of indexes where near match of searched value is found excluding the header row
    # The Excel columns start with 1, however when iterating, the tuples start with index 0
    _row_idx_list = [_xl_row_idx for _xl_row_idx, _row_val in
                     enumerate(self.my_base_active_ws.iter_rows(values_only=True), start=1) if
                     str(_search_val) in str(_row_val[_col_idx - 1]) if _xl_row_idx != _header_row_num]
    # Return type is list
    return _row_idx_list
    