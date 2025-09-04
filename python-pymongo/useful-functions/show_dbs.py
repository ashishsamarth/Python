def show_dbs(self):
    '''
    Method to see existing database in connected Mongo Instance
    '''
    return self.my_client.list_database_names()
