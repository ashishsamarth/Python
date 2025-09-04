def get_row_val_based_on_search_param_in_col(self, _col_name, _search_val):
    '''
    Method to get row values based on a search param in a given column name
    Arguments to this method are: - Column name to be searched and search value
    '''
    _col_idx = self.get_col_idx_by_name(_col_name)
    # Return the entire row, if searched value was found in the given column

    return [_ for _ in self.my_df.itertuples() if _[_col_idx + 1] == _search_val]
