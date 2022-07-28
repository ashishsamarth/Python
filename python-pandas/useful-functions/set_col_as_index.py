# Method to set a column as the index column
# Argument to this method is: - Column name which needs to be set as index
def set_col_as_index(self, _col_name):
    return self.my_df.set_index(_col_name)