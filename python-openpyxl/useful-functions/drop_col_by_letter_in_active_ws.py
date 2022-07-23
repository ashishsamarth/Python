from openpyxl.utils import column_index_from_string
# Method to drop the column by column letter
# Arguments to this method are:- Row number for header row, worksheet name and column letter
def drop_col_by_letter_in_active_ws(self, _header_row_num, _ws_name, _col_letter):
    # Activate the worksheet
    self.active_ws(_ws_name)
    # get the column index based on the column name
    _col_idx = column_index_from_string(_col_letter)
    # Delete the column using the column index
    self.my_base_active_ws.delete_cols(_col_idx, 1)
    # Save the workbook
    self.save_wb()