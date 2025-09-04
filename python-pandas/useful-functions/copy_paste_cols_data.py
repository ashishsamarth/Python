def copy_paste_cols_data(self, _src_col_name, _tgt_col_name):
    '''
    Method to copy the contents from one column to another column of dataframe
    Arguments to this method are source column name and target column name
    # NOTE: - If target col does not exist in the dataframe, it will be created at run time
    '''
    try:
        self.my_df[_tgt_col_name] = self.my_df[_src_col_name]
    except KeyError:

        print(f' Source column :- "{_src_col_name}"  not found in worksheet')
