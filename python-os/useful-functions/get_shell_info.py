# Method to get the shell
# Assumption: OS is Linux
def get_shell_info(self):
    if self.os_type == 'Linux':
        return os.environ['SHELL'].split('/')[-1]
        