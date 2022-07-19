# Method to release connections back to pool
# Argument to this method:- None
def db_release_conn_to_pool(self):
    self.pool.release(self.db_auto_connect)