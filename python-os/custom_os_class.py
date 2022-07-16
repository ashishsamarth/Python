import os
import sys


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomOs:


    # Initialize the class with filepath and filename
    def __init__(self, _my_file_path, _my_file_name):
        self.my_filepath = _my_file_path
        self.my_filename = _my_file_name
        self.current_directory = os.getcwd()
    
    # Method to navigate into a target directory
    # This method utilizes the file path captured during class initialization
    def change_dir(self):
        os.chdir(self.my_filepath)
    
    # Method to rename the files
    @staticmethod
    def rename_files(self, _current_file_name, _new_file_name):
        os.renames(_current_file_name, _new_file_name)
    
    # Method to list the contents of the directory
    # Note: listdir() does not need an argument
    @staticmethod
    def dir_contents(self):
        os.listdir()
    
    # Method to go back n number of directories
    # Argument to this method is: number (integer) of directories to go back
    def go_back_n_dirs(self, num_of_dirs: int):
        # method variable to hold the message
        note = 'Input Argument must be valid integer'
        try:
            # Validate if the input argument is indeed an integer
            # if not, Assertion Error will be generated, along with message printed (note) and execution will move to except block
            assert isinstance(num_of_dirs, int), note
            # build the navigation command using string concatenation
            navigation = ('..\\' * num_of_dirs).rstrip('\\')
            # Change the directory based on navigation variable
            os.chdir(navigation)
            # assign the current directory variable in __init__ to actual current directory
            