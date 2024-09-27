from openpyxl.utils import column_index_from_string
# Method to drop column by name
# Arguments to this method are:- Row number for header row, worksheet name and column name
def drop_col_by_name_in_active_ws(self, _header_row_num, _ws_name, _col_name):
    # Activate the worksheet
    self.active_ws(_ws_name)
    # get the column index based on the column name
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # Delete the column using the column index
    self.my_base_active_ws.delete_cols(_col_idx, 1)
    # Save the workbook
    self.save_wb()