# Method to close the session
# Call the shutdown method on the session
def db_session_close(self):
    self.db_session().shutdown()