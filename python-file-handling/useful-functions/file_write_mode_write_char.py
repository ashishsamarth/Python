# Method to write to file in newlines
def file_write_mode_write_char(self, data_set, in_newline):
    # open the filename captured during initialization in write mode
    with open(self.my_filename, 'w') as write_mode:
        # Based on the value provided for argument in_newline the text will be written with or without newline
        if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
            write_mode.write(data_set + '\n')
        elif in_newline in ['n','N','NO', 'No', 'no']:
            write_mode.write(data_set)