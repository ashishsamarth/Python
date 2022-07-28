# Method to get count of unique items in a given column
# Argument to this method is: - Column name
def get_unique_value_count_in_col(self, _col_name):
    return self.my_df[_col_name].nunique()