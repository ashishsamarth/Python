# Method to get frequency of occurrences per unique item in a given column
# Argument to this method is: - Column index position
def value_frequency_in_col_by_idx(self, _col_idx):
    return self.my_df[self.my_df_col_idx_name[_col_idx]].value_counts()