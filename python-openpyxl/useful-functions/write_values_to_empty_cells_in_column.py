from openpyxl.utils import column_index_from_string
# Method to write static value to empty cells in a given column
# Arguments to this method are:- Row number of the header wow, Column name and static to be written
def write_values_to_empty_cells_in_column(self, _header_row_num, _col_name, _write_val):
    # Fetch the column index from column name using 'ref_col_name_letter_map' method
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    for _row_idx in self.get_row_idx_lst_of_empty_rows_specific_col(_header_row_num, _col_name):
        # write user defined value to the cells at specific row indexes
        self.my_base_active_ws.cell(row=_row_idx, column=_col_idx).value = _write_val
    # save workbook
    self.save_wb()