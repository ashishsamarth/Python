# Method to delete a row based on row index
def del_row_by_idx(self, _row_idx):
    return self.my_base_active_ws.delete_rows(_row_idx)