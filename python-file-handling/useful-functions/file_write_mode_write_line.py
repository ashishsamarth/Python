# Method to write user provided text to a file in single line followed by a new line character
def file_write_mode_write_line(self, _text, in_newline):
    with open(self.my_filename, 'w') as write_mode:
        # Based on the value provided for argument in_newline the text will be written with or without newline
        if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
            write_mode.writelines(_text + '\n')
        elif in_newline in ['n','N','NO', 'No', 'no']:
            write_mode.writelines(_text)