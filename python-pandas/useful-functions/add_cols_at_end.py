# Method to add multiple columns with no-values to the dataframe (or excel)
# Note: _col_names must be an iterable preferable a list
def add_cols_at_end(self, _col_names):
    # following line will add the new columns, only if they do not exist already
    # The list comprehension provides the string of column names
    # The columns are added without any value hence ' = '' '
    self.my_df[[str(_) for _ in _col_names if _ not in self.my_df.columns]] = ''
    return self.my_df
