# Method to get the DB version of the connected DB
# Argument to this method: None
def db_version(self):
    return self.db_auto_connect.version