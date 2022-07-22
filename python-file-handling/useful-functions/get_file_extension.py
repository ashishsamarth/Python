# Method to get the file extension using the split method of class <str>
def get_file_extension(self):
    my_file_extension = self.my_filename.split('.')[-1]
    # This will only return the result and does not perform printing
    return my_file_extension