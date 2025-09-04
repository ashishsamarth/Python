def value_frequency_in_col_by_name(self, _col_name):
    '''
    Method to get frequency of occurrences per unique item in a given column
    Argument to this method is: - Column index position
    '''
    return self.my_df[_col_name].value_counts()
