def create_new_wb(self, _file_location, _wb_name, _ws_name):
    '''
    Method to create a new workbook using an exsting instantiated object
    Arguments to this Method: Destination Directory, Workbok name, Worksheet name
    '''
    # Create a workbook object
    _wb = openpyxl.Workbook()
    # Workbook will have atleast one worksheet
    _ws = _wb.active
    # Rename the worksheet with the name provided as an argument
    _ws.title = _ws_name
    # Save the newly created workbook
    _wb.save(filename=_file_location+_wb_name)
    return 'f New Workbook created with name:- {_wb_name}'