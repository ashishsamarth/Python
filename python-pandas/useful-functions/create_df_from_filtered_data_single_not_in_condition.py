import pandas as pd
# Method to create dataframe with based on one condition at column level
# Arguments to this method are: - Column name where condition is to be applied, and the condition itself
def create_df_from_filtered_data_single_not_in_condition(self, _column_name, _condition):
    # create a new filtered dataset based on the condition applied on the column
    _filtered_data_set = (self.my_df.loc[self.my_df[_column_name] != _condition])
    # return Dataframe
    return pd.DataFrame(_filtered_data_set)