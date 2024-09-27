# Method to close the connection of connected Mongo instance
def connection_close(self):
    self.my_client.close()