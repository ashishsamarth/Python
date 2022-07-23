# Method to create a new worksheet in workbook
# Argument to this method is: - New worksheet name
def add_new_ws_at_end_of_wb(self, _new_ws_name):
    # New worksheet will be added to workbook, only if it doesn't exist already
    if not self.if_ws_in_wb(_new_ws_name):
        self.my_base_wb.create_sheet(_new_ws_name)
        self.save_wb()
