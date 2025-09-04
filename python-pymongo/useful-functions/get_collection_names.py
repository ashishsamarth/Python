def get_collection_names(self):
    '''
    Method to get the collection names for a connected DB of Mongo Instance
    '''
    return self.connected_db.list_collection_names()
