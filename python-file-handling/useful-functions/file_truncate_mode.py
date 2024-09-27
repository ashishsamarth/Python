# Method to truncate the file using the append mode
def file_truncate_mode(self):
    with open(self.my_filename, 'a') as truncate_mode:
        truncate_mode.truncate(0)