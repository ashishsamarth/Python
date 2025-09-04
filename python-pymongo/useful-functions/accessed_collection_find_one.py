def accessed_collection_find_one(self, _collection_name):
    '''
    Method to see one sample document from a given collection name
    Argument to this method: Collection Name
    '''
    note = 'Collection Name provided is not a present in Connected Database'
    # Assert if the provided collection name exists in the connected DB
    assert _collection_name in self.get_collection_names(), note
    # In case of Assertion error, the collection cannot be accessed
    _my_collection = self.connected_db[_collection_name]
    # return type is dict

    return _my_collection.find_one()
