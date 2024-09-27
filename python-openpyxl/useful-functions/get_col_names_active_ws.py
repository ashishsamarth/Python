# Method to get column names of the active worksheet
def get_col_names_active_ws(self, _header_row_num):
    _col_names = [_ for _ in self.ref_col_idx_name_map(_header_row_num).values()]
    # Return type is a list
    return _col_names