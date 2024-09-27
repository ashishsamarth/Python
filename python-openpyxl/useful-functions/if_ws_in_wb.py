# Method to check if a given worksheet exists in workbook
# Argument to this method is: workbook name
def if_ws_in_wb(self, _ws_name):
    # if worksheet exists in list of worksheets of workbook returns True else False
    if _ws_name in self.ws_names_in_my_base_wb:
        return True
    return False