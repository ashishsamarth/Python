# Import os package
import os
# Import shutil package to deal with copy / paste needs
import shutil
# Note pwd is only available for unix like os
# if you wish to use pwd module for windows, try winpwd
from pwd import getpwuid
from time import ctime

# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomOs:


    # Initialize the class with filepath and filename
    def __init__(self, _my_file_path, _my_file_name):
        self.my_filepath = _my_file_path
        self.my_filename = _my_file_name
        # Get the current working directory
        self.current_directory = os.getcwd()
        # Get the OS type name
        self.os_type = os.uname().sysname
        # Get the OS distribution name
        self.os_distrib = os.uname().nodename
        # Get the OS Machine name
        self.os_machine = os.uname().machine
    
    # Method to get the shell
    # Assumption: OS is Linux
    def get_shell_info(self):
        if self.os_type == 'Linux':
            return os.environ['SHELL'].split('/')[-1]
    
    # Method to get disk information
    def get_disk_info():
        # Capture the disk usage in three different variable (Note these are in bytes)
        total_b, used_b, available_b = shutil.disk_usage('.')
        gb = 10 ** 9
        # Convert bytes to gigabytes
        total_gb = '{:6.2f} GB'.format(total_b / gb)
        used_gb = '{:6.2f} GB'.format(used_b / gb)
        available_gb = '{:6.2f} GB'.format(available_b / gb)
        # Create a dictionary with the information
        disk_info={'Total': total_gb,
               'Used': used_gb,
               'Available': available_gb}
        return disk_info

    # Method to get file metadata
    # Argument to this method: input filename
    def get_file_metadata(self):
        file_metadata = {'File_Name': self.my_filename,
                     'File_Owner_username': getpwuid(os.stat(self.my_filename).st_uid).pw_name,
                     'File_Owner_name': getpwuid(os.stat(self.my_filename).st_uid).pw_gecos,
                     'Created': ctime(os.stat(self.my_filename).st_ctime),
                     'Accessed': ctime(os.stat(self.my_filename).st_atime),
                     'Modified': ctime(os.stat(self.my_filename).st_mtime)
                     }
        return file_metadata

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
            self.current_directory=os.getcwd()
            # return type of this method is string
            return f'Navigated Back to {self.current_directory}'
        except AssertionError:
            return note