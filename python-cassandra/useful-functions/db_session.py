# 
def db_session(self):
    '''
    Method to connect to Cassandra Cluster on the remote host
    '''
    # Read the host, port and authorization params from the config file
    # The configurations must match with ~.cassandra/cqlshrc on server
    cluster = Cluster([self.host], port=self.port, auth_provider=self.auth)
    # connect to the cluster and get the session
    session = cluster.connect(self.my_keyspace)
    return session