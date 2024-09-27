def exec_select_return_named_tuple_fetch_all(self, _query):
    '''
    Method to execute a cql query
    Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
    '''
    session = self.db_session()
    # This line sets up the return type of the query as a named tuple
    session.row_factory = named_tuple_factory
    row_result_as_named_tuple = session.execute(_query).all()
    # return type of this method is a list of named tuples
    return row_result_as_named_tuple     