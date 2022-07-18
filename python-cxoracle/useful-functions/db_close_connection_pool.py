# Method to close the connection pool
# Argument to this method:- None
def db_close_conn_pool(self):
    self.pool.close()