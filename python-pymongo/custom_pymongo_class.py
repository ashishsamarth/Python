from pymongo import MongoClient
from bson.objectid import ObjectId
import db_conf
from pprint import pprint

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
        self.client_host = ''
        self.mongo_server_version = ''
        self.conn_status = ''
        self.connected_as = ''
        self.connected_db = ''

    # usage: my_obj = CustomPymongo(**db_conf.python_api_connect)

    # Method to see existing database in connected Mongo Instance
    def show_dbs(self):
        return self.my_client.list_database_names()

    # Method to connect (use) specific Mongo-DB or Schema
    # Argument to this method is:- Database Name
    def connect_db(self, _db_name):
        note = 'Database Name provided, does not exist in connected Mongo Instance'
        assert _db_name in self.show_dbs(), note
        # following line connects to the user provided DB, only if its a existing DB in mongo instance
        _my_db = self.my_client[_db_name]
        # Set the value of following property in __init__() with the user provided database name
        self.connected_db = _my_db
        # Following property will provide the host name of client machine
        self.client_host = self.connected_db.command('serverStatus')['host']
        # Following property will provide the version number for connected MongoDB Instance
        self.mongo_server_version = self.connected_db.command('serverStatus')['version']
        # Following property will provide the process id
        self.process_id = self.connected_db.command('serverStatus')['pid']
        # Following property will provide the connection status
        # Return type is a dictionary, key = 'ok' and value = 1.0 indicates to successful connection
        self.conn_status = self.connected_db.command('connectionStatus')
        # Following property provides the username of the connected user
        self.connected_as = 'Connected to DB as :- ' + self.connected_db.command('connectionStatus')['authInfo']['authenticatedUsers'][0]['user']
        # return type of this method is the DB instance
        return _my_db

    # Method to get the collection names for a connected DB of Mongo Instance
    def get_collection_names(self):
        return self.connected_db.list_collection_names()

    # Method to access a collection in connected DB of Mongo Instance
    # Argument to this method: A valid collection name
    def accessed_collection(self, _collection_name):
        note = 'Collection Name provided is not a present in Connected Database'
        assert _collection_name in self.get_collection_names(), note
        # In case of Assertion error, the collection cannot be accessed
        _my_collection = self.connected_db[_collection_name]
        return _my_collection

    # Method to see one sample document from a given collection name
    # Argument to this method: Collection Name
    def accessed_collection_find_one(self, _collection_name):
        note = 'Collection Name provided is not a present in Connected Database'
        # Assert if the provided colleciton name exists in the connected DB
        assert _collection_name in self.get_collection_names(), note
        # In case of Assertion error, the collection cannot be accessed
        _my_collection = self.connected_db[_collection_name]
        # return type is dict
        return _my_collection.find_one()

    # Method to execute specific DB commands on connected database
    # Argument to this method: DB command
    # Reference URL for list of executable commands:- "https://www.mongodb.com/docs/manual/reference/command/"
    def db_execute_command(self, _command):
        return self.connected_db.command(_command)

    # Method to close the connection of connected Mongo instance
    def connection_close(self):
        self.my_client.close()

# _my_obj = CustomPymongo(**db_conf.python_api_connect)
# pprint(_my_obj.show_dbs())
# pprint(_my_obj.connect_db('development'))
# pprint(_my_obj.accessed_collection('zips'))    