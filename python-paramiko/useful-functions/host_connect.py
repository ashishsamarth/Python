def host_connect(self):
    '''
    Method to remotely connect to host
    Argument to this method is: Hostname, Username and Location of Private Key for authentication
    '''
    return self.ssh.connect(hostname=self.hostname, username=self.username, key_filename = self.key_filename)
