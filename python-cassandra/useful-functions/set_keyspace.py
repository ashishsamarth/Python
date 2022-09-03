# 
def set_keyspace(self, _keyspace_name):
    '''
    Method to set the user provided keyspace name
    '''
    # Update the __init__ property to be used during session creation for keyspace
    # This approach is also helpful for query execution without passing the keyspace everytime
    self.my_keyspace = _keyspace_name
    return self.my_keyspace