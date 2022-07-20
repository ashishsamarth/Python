# Method to access a collection in connected DB of Mongo Instance
# Argument to this method: A valid collection name
def accessed_collection(self, _collection_name):
    note = 'Collection Name provided is not a present in Connected Database'
    assert _collection_name in self.get_collection_names(), note
    # If case of Assertion error, the collection cannot be accessed
    _my_collection = self.connected_db[_collection_name]
    return _my_collection