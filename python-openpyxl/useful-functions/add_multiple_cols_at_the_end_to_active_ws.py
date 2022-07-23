# Method to add multiple columns with names as the last column of active worksheet
# Arguments to this method are:- Column Names (as an iterable), and row number of header row
def add_multiple_cols_at_the_end_to_active_ws(self, _header_row_num, _col_names):
    # Iterate over the values in the iterable (column name)
    for _ in _col_names:
        if _ not in self.get_col_names_active_ws(_header_row_num):
            # call the function 'add_new_col_at_the_end_to_active_ws' and pass the column name
            self.add_new_col_at_the_end_to_active_ws(_header_row_num, _)
            # Most important step is to reload the workbook, so that changes from last iteration are reloaded
            self.reload_wb()
        # This method calls save internally, hence its auto save from user perspective
        self.save_wb()