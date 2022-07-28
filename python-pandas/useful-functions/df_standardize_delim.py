# Method to standardize delimiter for scenarios where the dataset needs curation
# If the dataset has different delimiters
def df_standardize_delim(self, _col_name, _delim):
    to_replace = [", ", ",", "'", "; ", " ; ", " ", "\\", ";;", "-", "/", ",;"]
    for item in to_replace:
        # Assign the formatted value to the column
        self.my_df[_col_name] = self.my_df[_col_name].str.replace(item, _delim, regex=True)
    return self.my_df[_col_name]