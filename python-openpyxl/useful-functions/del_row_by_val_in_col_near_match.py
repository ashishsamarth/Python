# Method to delete rows based on a near match of cell value in a given column
# Argument to this method are: - Row number of the header row, Column name and cell value
def del_row_by_val_in_col_near_match(self, _header_row_num, _col_name, _search_val):
    # Check if provided column name exists in the worksheet using 'ref_col_name_idx_map' method
    # 'ref_col_name_idx_map' method has return type of dict
    if _col_name in self.ref_col_name_idx_map(_header_row_num).keys():
        # Check if the value provided has a near match in the given column
        if self.get_row_idx_lst_based_on_search_val_specific_col_near_match(_header_row_num, _col_name,
                                                                            _search_val):
            # Get the list of indexes based on match condition
            _depleting_idx = [_ for _ in
                              self.get_row_idx_lst_based_on_search_val_specific_col_near_match(_header_row_num,
                                                                                               _col_name,
                                                                                               _search_val)]
            # Iterate for all values in _depleting_idx
            while _depleting_idx:
                # Delete the row for the iterated index value
                # Start from the last index value since it will not change position of index, post delete
                # Deletion of row from top will move the following row one row up there by changing the index
                # Causing incorrect row to be deleted starting from 2nd iteration
                self.my_base_active_ws.delete_rows(_depleting_idx[-1])
                # Save the workbook
                self.save_wb()
                # delete the last element from the index to deplete the iteration count
                del _depleting_idx[-1]