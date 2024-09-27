from openpyxl.utils import column_index_from_string
# Method to get row indexes of empty rows in a specific column
# Arguments to this method are: - Row number of header row and Column name
def get_row_idx_lst_of_empty_rows_specific_col(self, _header_row_num, _col_name):
    # Fetch the column index from column name using 'ref_col_name_idx_map' method
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # Get the list of indexes of empty rows excluding the header row
    _row_idx_list = [_xl_row_idx for _xl_row_idx, _row_val in
                     enumerate(self.my_base_active_ws.iter_rows(values_only=True), start=1) if
                     not _row_val[_col_idx - 1]]
    # Return type is list
    return _row_idx_list