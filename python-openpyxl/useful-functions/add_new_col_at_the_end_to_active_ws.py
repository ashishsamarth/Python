# Method to add a new column with name as the last column of active worksheet
# Arguments to this method are: - New column name and row number of header row
def add_new_col_at_the_end_to_active_ws(self, _header_row_num, _new_col_name):
    # New column will be added only if, it does not exist already
    if _new_col_name not in self.get_col_names_active_ws(_header_row_num):
        # Note:- Since we are adding the column at the end, we need to auto identify its index
        # We are using the existing max_column property of the worksheet and incrementing it by 1
        _new_col_idx = self.my_base_active_ws_max_col + 1
        # Once the columns is added, we correctly identify the cell where the column name will be written
        self.my_base_active_ws.cell(row=_header_row_num, column=_new_col_idx).value = _new_col_name
        # This method calls save internally, hence its auto save from user perspective
        self.save_wb()