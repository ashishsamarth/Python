# Method to connect (use) specific Mongo-DB or Schema
# Argument to this method is:- Database Name
def connect_db(self, _db_name):
    note = 'Database Name provided, does not exist in connected Mongo Instance'
    assert _db_name in self.show_dbs(), note
    # following line connects to the user provided DB, only if its a existing DB in mongo instance
    _my_db = self.my_client[_db_name]
    # Set the value of following property in __init__() with the user provided database name
    self.connected_db = _my_db
    # return type of this method is the DB instance
    return _my_db