from pymongo import MongoClient
import db_conf


class CustomPymongo:

    # Initialize the class with **kwargs containing the parameters (host, port, username, password, authsource & authMechanism)
    def __init__(self, **connection_params):
        self.my_client = MongoClient(host=connection_params.get('host') + ':' + str(connection_params.get('port')),
                                     username=connection_params.get(
                                         'username'),
                                     password=connection_params.get(
                                         'password'),
                                     authSource=connection_params.get(
                                         'authSource'),
                                     authMechanism=connection_params.get('authMechanism'))
        # Following line provide information on the connection params and the connected database
        self.my_db = self.my_client['__my_database__']
        # Initialize the following property as <blank>, this is set by connect_db() and then used in consequent methods
        self.connected_db = ''

    # usgae: my_obj = CustomPymongo(**db_conf.python_api_connect)