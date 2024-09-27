# Method to copy data from source worksheet to target worksheet
# Arguments to this method are: -  source worksheet name and target worksheet name
# Note: This method will create a new worksheet, if the target worksheet does not exist
def copy_ws_src_to_tgt(self, _src_ws, _tgt_ws):
    # Code block will only proceed if source worksheet exists
    if self.if_ws_in_wb(_src_ws):
        # If the target worksheet exists, code will proceed to iterations and copy
        if self.if_ws_in_wb(_tgt_ws):
            pass
        # If the target worksheet does not exist, new worksheet will be created
        # Name of newly created worksheet will the 2nd argument
        else:
            self.add_new_ws_at_end_of_wb(_tgt_ws)
            # Once the target worksheet is added, save the workbook
            self.save_wb()
        # Special Note: If we use iterrows() or itercolumns() the cell value assignment fails
        # Since the active keyword is not used for sheet activation
        # iterate over the number of columns  in source
        for _row in range(1, self.my_base_wb[_src_ws].max_row + 1):
            # Iterate over the number of rows in source
            for _col in range(1, self.my_base_wb[_src_ws].max_column + 1):
                # Assign the values to each target cell from source cell
                self.my_base_wb[_tgt_ws].cell(row=_row, column=_col).value = self.my_base_wb[_src_ws].cell(row=_row,
                                                                                                           column=_col).value
        self.save_wb()