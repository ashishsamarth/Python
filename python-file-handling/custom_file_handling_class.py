# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomFileHandler:

    # Initialize the class with filename
    def __init__(self, _my_file_name):
        self.my_filename = _my_file_name

    # Method to get the file extension using the split method of class <str>
    def get_file_extension(self):
        my_file_extension = self.my_filename.split('.')[-1]
        # This will only return the result and does not perform printing
        return my_file_extension

    # Method to read the file, default num of lines is 0
    def file_read_mode_read_line(self, num_of_lines=0):
        # open the filename captured during initialization in read mode
        with open(self.my_filename, 'r') as read_mode:
            # The default value of argument num_of_lines is zero, so following line of code will only read one line
            single_line = read_mode.readline()
            # If the value for # of lines is provided, it will be passed to the code and that many lines will be read
            if num_of_lines > 0:
                multilines = read_mode.readlines(num_of_lines)
                # _ is a temp operator which will not be used outside the context of for loop
                for _ in multilines:
                    print(_)
            else:
                print(single_line)

    # Method to read  the characters from the file based on user input
    def file_read_mode_read_char(self, num_of_characters=5):
        with open(self.my_filename, 'rt', encoding='utf8') as read_char:
            # The default value of argument num_of_characters is set to 5, in case the user does not provide the value
            # Meaning if the method is called without passing the argument, the method will return first 5 characters from the file
            return read_char.read(num_of_characters)

    # Method to write to file in newlines
    def file_write_mode_write_char(self, data_set, in_newline):
        # open the filename captured during initialization in write mode
        with open(self.my_filename, 'w') as write_mode:
            # Based on the value provided for argument in_newline the text will be written with or without newline
            if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
                write_mode.write(data_set + '\n')
            elif in_newline in ['n','N','NO', 'No', 'no']:
                write_mode.write(data_set)

     # Method to write user provided text to a file in single line followed by a new line character
    def file_write_mode_write_line(self, _text, in_newline):
        with open(self.my_filename, 'w') as write_mode:
            # Based on the value provided for argument in_newline the text will be written with or without newline
            if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
                write_mode.writelines(_text + '\n')
            elif in_newline in ['n','N','NO', 'No', 'no']:
                write_mode.writelines(_text)

    # Method to truncate the file using the append mode
    def file_truncate_mode(self):
        with open(self.my_filename, 'a') as truncate_mode:
            truncate_mode.truncate(0)

    # Method to append the text to file
    def file_append_mode(self, data_set, in_newline):
        # open the filename captured during initialization in append mode
        with open(self.my_filename, 'a') as append_mode:
            # Based on the value provided for argument in_newline the text will be written with or without newline
            if in_newline in ['y', 'Y','Yes', 'YES', 'yes']:
                append_mode.write(data_set + '\n')
            elif in_newline in ['n','N','NO', 'No', 'no']:
                append_mode.write(data_set)

    # Method to separate the text printed on the terminal
    @staticmethod
    def display_separator():
        print('----XXXX'*6)