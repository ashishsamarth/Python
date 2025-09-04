def add_col_by_idx(self, position, _col_name):
    '''
    Method to add a new column using the index position in the existing dataframe
    '''
    # The following statement checks if the user provided column name already exists in the dataframe or not
    # The new column will only be added if it does not exist already
    if _col_name not in self.my_df.columns:
        return self.my_df.insert(position, _col_name, '', True)
    # Else the new column name will not be added to the dataframe
    else:
        print(f'Column :- "{_col_name}" is already present in the Dataframe, skipping addition...', end='\n')

