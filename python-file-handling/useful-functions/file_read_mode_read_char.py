# Method to read  the characters from the file based on user input
def file_read_mode_read_char(self, num_of_characters=5):
    with open(self.my_filename, 'rt', encoding='utf8') as read_char:
        # The default value of argument num_of_characters is set to 5, in case the user does not provide the value
        # Meaning if the method is called without passing the argument, the method will return first 5 characters from the file
        return read_char.read(num_of_characters)