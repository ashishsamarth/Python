# 
# Call the shutdown method on the session
def db_session_close(self):
    '''
    Method to close the session
    
    '''
    self.db_session().shutdown()