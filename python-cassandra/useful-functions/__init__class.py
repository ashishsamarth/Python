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
    def __init__(self, **cassandra_params):
        self.auth = PlainTextAuthProvider(username = cassandra_params.get('cassandra_user'), 
                                            password = cassandra_params.get('cassandra_password'))
        self.host = cassandra_params.get('cassandra_host')
        self.port = cassandra_params.get('cassandra_port')
        self.my_keyspace = ''