# Method to get the unique values from a given column
# Argument to this method is: - Column name
def get_col_unique_values_by_name(self, _col_name):
    # Return type is dependent on column values
    return self.my_df[_col_name].unique()