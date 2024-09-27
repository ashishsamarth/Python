# Method to see existing database in connected Mongo Instance
def show_dbs(self):
    return self.my_client.list_database_names()