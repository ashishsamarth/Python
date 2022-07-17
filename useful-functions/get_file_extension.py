# Method to get the file extension
# Argument to the method: filename
def get_file_extension(self, _filename):
    # Using the split method of class <str>
    # split the filename using '.' and capturing the last element of the return type class <list>
    self.file_ext = _filename.split('.')[-1]
    return self.file_ext
