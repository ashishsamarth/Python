# Method to rename an existing column
# Arguments to this method are: - Old column name and New Column Name
def rename_col(self, _old_col_name, _new_col_name):
    try:
        # Assign the renamed columns to original dataframe
        # so that changes are reflected in spreadsheet
        self.my_df = self.my_df.rename(columns={_old_col_name: _new_col_name})
    except KeyError:
        print(f' Column Name :- "{_old_col_name}" not found in the dataframe')