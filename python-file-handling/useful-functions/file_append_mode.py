# Method to append the text to file
def file_append_mode(self, data_set, in_newline):
    # open the filename captured during initialization in append mode
    with open(self.my_filename, 'a') as append_mode:
        # Based on the value provided for argument in_newline the text will be written with or without newline
        if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
            append_mode.write(data_set + '\n')
        elif in_newline in ['n','N','NO', 'No', 'no']:
            append_mode.write(data_set)