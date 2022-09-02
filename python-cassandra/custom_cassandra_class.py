# Import cassandra - python driver
# Import cluster package from cassandra module to manage connection
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
# following modules are part of row-factory which changes the return type of the query
# The default return type for this module is tuple, however to match your scenario their are three options available
# understanding of these will remove the need of explicit data type conversion
from cassandra.query import tuple_factory, named_tuple_factory, dict_factory, ordered_dict_factory
# Import cassandra_conf : This holds the connection params
import cassandra_conf


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomCassandra:

    # Initialize the class to set the SSH client and set up host addition policy
    # Arguments to this method is - **kwargs
    # **Key word argument (has three params, user, password and the location of private key)
    # Default data type of response is a named_tuple, which allows accessing the columns using col names instead of index
    def __init__(self, **cassandra_params: dict):
        self.auth = PlainTextAuthProvider(username = cassandra_params.get('cassandra_user'), password = cassandra_params.get('cassandra_password'))
        self.host = cassandra_params.get('cassandra_host')
        self.port = cassandra_params.get('cassandra_port')
        self.my_keyspace = ''
    
    # Method to set the user provided keyspace name
    def set_keyspace(self, _keyspace_name: str):
        # Update the __init__ property to be used during session creation for keyspace
        # This approach is also helpful for query execution without passing the keyspace everytime
        self.my_keyspace = _keyspace_name
        return self.my_keyspace
    
    # Method to connect to Cassandra Cluster on the remote host
    def db_session(self):
        # Read the host, port and authorization params from the config file
        # The configurations must match with ~.cassandra/cqlshrc on server
        cluster = Cluster([self.host], port=self.port, auth_provider=self.auth)
        # connect to the cluster and get the session
        session = cluster.connect(self.my_keyspace)
        return session
    
    # Method to execute a cql query
    # Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
    def exec_select_return_tuple_fetch_one(self, _query):
        session = self.db_session()
        # This line sets up the return type of the query as a tuple
        session.row_factory = tuple_factory
        row_result_as_tuple = session.execute(_query).one()
        # return type of this method is a tuple
        return row_result_as_tuple

    # Method to execute a cql query
    # Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
    def exec_select_return_tuple_fetch_all(self, _query):
        session = self.db_session()
        # This line sets up the return type of the query as a tuple
        session.row_factory = tuple_factory
        row_result_as_tuple = session.execute(_query).all()
        # return type of this method is a list of tuples
        return row_result_as_tuple

    # 
    # 
    def exec_select_return_named_tuple_fetch_one(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as a named tuple
        session.row_factory = named_tuple_factory
        row_result_as_named_tuple = session.execute(_query).one()
        # return type of this method is a named tuple
        return row_result_as_named_tuple

    def exec_select_return_named_tuple_fetch_all(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as a named tuple
        session.row_factory = named_tuple_factory
        row_result_as_named_tuple = session.execute(_query).all()
        # return type of this method is a list of named tuples
        return row_result_as_named_tuple        
    
    def exec_select_return_dict_fetch_one(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as a dictionary
        session.row_factory = dict_factory
        row_result_as_dict = session.execute(_query).one()
        # return type of this method is a dictionary
        return row_result_as_dict

    def exec_select_return_dict_fetch_all(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as a dictionary
        session.row_factory = dict_factory
        row_result_as_dict = session.execute(_query).all()
        # return type of this method is a list of dictionaries
        return row_result_as_dict

    def exec_select_return_ordered_dict_fetch_one(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as an ordered dictionary
        session.row_factory = ordered_dict_factory
        row_result_as_ordered_dict = session.execute(_query).one()
        # return type of this method is an ordered dictionary
        return row_result_as_ordered_dict

    def exec_select_return_ordered_dict_fetch_all(self, _query):
        '''
        Method to execute a cql query
        Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
        '''
        session = self.db_session()
        # This line sets up the return type of the query as an ordered dictionary
        session.row_factory = ordered_dict_factory
        row_result_as_ordered_dict = session.execute(_query).all()
        # return type of this method is a list of ordered dictionaries
        return row_result_as_ordered_dict

    def db_session_close(self):
        '''
        Method to close the session
        Call the shutdown method on the session
        '''
        self.db_session().shutdown()