# Method to save the workbook to new file
# Argument for this method is: - New File Name
def save_wb_as_new_file(self, _new_file_name):
    assert _new_file_name.split('.')[-1] in ['xls', 'xlsx'], 'Input file does not have valid excel extension'
    return self.my_base_wb.save(_new_file_name)