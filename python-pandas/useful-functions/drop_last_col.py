# Method to drop the last columns in the dataframe
# Note: This method assumes that there's at least 1 column in the dataframe
def drop_last_col(self):
    if len(self.my_df.columns.values) > 0:
        self.my_df.drop(self.my_df.columns[-1], axis=1, inplace=True)
    return 'dataframe is empty'