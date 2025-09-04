def df_sort_row_level_diff_cols(self, _src_col_name, _tgt_col_name, _delim, _sort_type,
                                _str_join_param):
    '''
    Method to sort data in a column at row level (basically each cell of a column)
    It has five arguments
    source column name:- The columns which has the unsorted data
    target column name:- The column where sorted data will be written
    _delim:- The current delimiter of the dataset in the cell
    _sort_type:- Can be 'asc' or 'desc'
    _str_join_param:- User provided _delim to join the strings
    Important Note:- This method can take care of both sorting and writing the data
                  and avoids the need of copying the data to target column before sorting
    '''
    for item in range(0, self.my_df[_src_col_name].shape[0]):
        if _sort_type == 'asc':
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # LHS:- Following line accesses the particular cell
            # item is row index and _col_name is column index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_position, column_position]
            self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=False))
        elif _sort_type == 'desc':
            self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=True))

    return self.my_df
