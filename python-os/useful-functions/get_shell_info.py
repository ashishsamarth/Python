def get_shell_info(self):
    '''
    Method to get the shell
    Assumption: OS is Linux
    '''
    if self.os_type == 'Linux':
        return os.environ['SHELL'].split('/')[-1]

        
