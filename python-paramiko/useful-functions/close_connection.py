# Method to close the connection of remote host
# Argument to this method is: None
def close_connection(self):
    return self.ssh.close()