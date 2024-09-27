# Method to convert multi-column values in to single column values from active worksheet
def convert_multi_col_val_to_single_col_in_active_ws(self):
    # Return a list of values
    return [_cell.value for _ in self.my_base_active_ws.columns for _cell in _]