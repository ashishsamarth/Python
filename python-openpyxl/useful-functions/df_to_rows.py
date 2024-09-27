from openpyxl import dataframe_to_rows
# Method to convert dataframe to excel rows
# Arguments to this method are: - Dataframe and Worksheet name
def df_to_rows(self, _dataframe, _ws_name):
    # Iterate over the rows in dataframe
    for _ in dataframe_to_rows(_dataframe, index=False):
        # Append the rows to worksheet
        self.my_base_wb[_ws_name].append(_)
    # Save workbook
    self.save_wb()