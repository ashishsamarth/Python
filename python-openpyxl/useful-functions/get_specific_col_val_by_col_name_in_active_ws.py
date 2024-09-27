from openpyxl.utils import column_index_from_string
# Method to get column values for a given column name
# Arguments to this method are:- Row number for header row & column name
def get_specific_col_val_by_col_name_in_active_ws(self, _header_row_num, _col_name):
    # Check if provided column name exists in the worksheet
    if _col_name in self.ref_col_idx_name_map(_header_row_num).values():
        # Fetch the values from the column provided
        # Skip the header row
        # Fetch the column index from column name using 'ref_col_name_letter_map' method
        return [_col_value[0] for _col_value in self.my_base_active_ws.iter_rows(min_row=_header_row_num + 1,
                                                                                 min_col=column_index_from_string(
                                                                                     self.ref_col_name_letter_map(
                                                                                         _header_row_num)[
                                                                                         _col_name]),
                                                                                 max_col=column_index_from_string(
                                                                                     self.ref_col_name_letter_map(
                                                                                         _header_row_num)[
                                                                                         _col_name]),
                                                                                 values_only=True)]