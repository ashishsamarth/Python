# Method to copy the header value from one worksheet to another
# Arguments to this method are: Row number of the header row, source worksheet name and target worksheet name
def copy_header_row_src_ws_to_tgt_ws(self, _header_row_num, _src_ws_name, _tgt_ws_name):
    # Capture the column names from the source worksheet names using list comprehension
    _src_col_name = [_ for _ in
                     self.my_base_wb[_src_ws_name].iter_rows(min_row=_header_row_num, max_row=(_header_row_num),
                                                             values_only=True)][0]
    # Iterate over the column names and the column indexes starting at position = 1
    for _col_idx, _col_val in enumerate(_src_col_name, start=1):
        # Write the column name to the target worksheet based on the iterated index and value
        self.my_base_wb[_tgt_ws_name].cell(row=_header_row_num, column=_col_idx).value = _col_val
    # Save the workbook    
    self.save_wb()