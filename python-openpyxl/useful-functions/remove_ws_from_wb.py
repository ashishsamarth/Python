# Method to remove a worksheet from a workbook
# Arguments to this method is: - worksheet name
def remove_ws_from_wb(self, _ws_name):
    try:
        del self.my_base_wb[_ws_name]
        self.save_wb()
        return '{} : worksheet removed successfully'.format(_ws_name)
    except KeyError:
        print('Worksheet by name:- "{}" was not found'.format(_ws_name))