# Method to add new column at specific index with a name
# Arguments to the method are: - New Column Name, New Column Position and row number for header
def add_new_col_at_specific_idx_to_active_ws(self, _header_row_num, _new_col_name, _idx_pos):
    # If the new column name already exists, nothing will be done
    if _new_col_name not in self.get_col_names_active_ws(_header_row_num):
        # Insert the column at the specific INDEX position
        # Note: The new column inserted will have a default cell value as None
        self.my_base_active_ws.insert_cols(_idx_pos)
        # Iterate over all the columns of the header row and select the exact cell based on the index position
        # Row number and Column number will provide the exact position
        for _row in self.my_base_active_ws.iter_cols(min_row=_header_row_num,
                                                     max_row=_header_row_num,
                                                     min_col=_idx_pos,
                                                     max_col=_idx_pos):
            for _cell in _row:
                if _cell.value is None:
                    # Update cell value to new column name
                    _cell.value = _new_col_name
                # This method calls save internally, hence its auto save from user perspective
                self.save_wb()