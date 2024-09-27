def active_ws(self, _ws_name):
    '''
    Method to set a specific worksheet as active where column names are in row#1
    Argument to this method is: - worksheet name
    '''
    # if the worksheet name exists in the workbook
    if self.if_ws_in_wb(_ws_name):
        # Activate a particular worksheet in a workbook
        # And assign it to the variable in __init__
        # This way, we will be able to use the 'my_base_active_ws' property
        # After object instantiation instead of having a new variable altogether
        self.my_base_active_ws = self.my_base_wb[_ws_name]
        # Expand the properties of the currently active worksheet back to __init__ variables
        self.my_base_active_ws_max_row = self.my_base_active_ws.max_row
        self.my_base_active_ws_max_col = self.my_base_active_ws.max_column
        self.my_base_active_ws_col_titles = [_col_name[0].value for _col_name in self.my_base_active_ws.iter_cols()]
    else:
        print('Worksheet {} not found in workbook'.format(_ws_name))