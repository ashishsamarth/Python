# Method to get row value by pandas row index
# Argument to this method is: - Row index of the pandas dataframe
# Note: Pandas row index is 2 + excel row index, since header row index is 0
# Pandas excludes the header row for df and starts with 0 for the first value row
def get_row_val_by_row_idx(self, _pandas_row_idx):
    return [_ for _ in self.my_df.itertuples()][_pandas_row_idx]