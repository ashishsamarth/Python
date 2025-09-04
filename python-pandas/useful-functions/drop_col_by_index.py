def drop_col_by_index(self, _col_idx):
    '''
    Method to remove a column using its existing position
    Note: This method is build using a try: except block to deal with index out of bounds exception    
    '''
    try:
        self.my_df.drop(self.my_df.columns[_col_idx], axis=1, inplace=True)
    except IndexError:
        print(
            f'ERROR: - Index value {_col_idx} is out of bounds, Current Index length is {self.my_df.shape[-1]}')

