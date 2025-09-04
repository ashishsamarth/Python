def execute_command(self, _command):
    '''
    Method to execute specific commands on the connected host
    Argument to this method is: command provided by end user
    '''
    stdin, stdout, stderr = self.ssh.exec_command(_command)
    command_output = stdout.read()

    return command_output
