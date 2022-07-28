# Method to get the values from a given column index position
# Return type is dependent on column values
def get_col_values_by_idx(self, _col_idx):
    return self.my_df[self.my_df_col_idx_name[_col_idx]]