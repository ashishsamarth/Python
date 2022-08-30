# 
def db_session_close(self):
    '''
    Method to close the session
    Call the shutdown method on the session
    '''
    self.db_session().shutdown()