# Method to reload the workbook after any value update or column additions
# No argument to this method
def reload_wb(self):
    # Call the initialization method with the file name to reload
    # since "openpyxl.load_workbook(self.my_filename, read_only=False)" is part of initialization
    self.__init__(self.my_filename)