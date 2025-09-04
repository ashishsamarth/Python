def close_connection(self):
    '''
    Method to close the connection of remote host
    Argument to this method is: None
    '''
    return self.ssh.close()
