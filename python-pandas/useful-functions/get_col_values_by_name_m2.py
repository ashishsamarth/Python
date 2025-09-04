def get_col_values_by_name_m2(self, _col_name):
    '''
    Method to get the values from a given column
    Argument to this method is: - Column name    
    '''
    # Return type is dependent on column values
    return self.my_df.get(_col_name)
