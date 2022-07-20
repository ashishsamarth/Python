# Method to get the collection names for a connected DB of Mongo Instance
def get_collection_names(self):
    return self.connected_db.list_collection_names()