import os
import sys


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomOs:

    # Initialize the class with filepath and filename
    def __init__(self, _my_file_path, _my_file_name):
        self.my_filepath = _my_file_path
        self.my_filename = _my_file_name
        self.current_directory = os.getcwd()