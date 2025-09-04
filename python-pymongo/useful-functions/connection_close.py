def connection_close(self):
    '''
    Method to close the connection of connected Mongo instance
    '''
    self.my_client.close()
