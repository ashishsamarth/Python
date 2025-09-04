import os

def go_back_n_dirs(self, num_of_dirs: int):
    '''
    Method to go back n number of directories
    Argument to this method is: number of directories to go back
    '''
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
