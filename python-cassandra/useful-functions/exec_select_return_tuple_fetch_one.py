from cassandra.query import tuple_factory

def exec_select_return_tuple_fetch_one(self, _query):
    '''
    Method to execute a cql query
    Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
    '''
    session = self.db_session()
    # This line sets up the return type of the query as a tuple
    session.row_factory = tuple_factory
    row_result_as_tuple = session.execute(_query).one()
    # return type of this method is a tuple
    return row_result_as_tuple