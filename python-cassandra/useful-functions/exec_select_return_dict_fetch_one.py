def exec_select_return_dict_fetch_one(self, _query):
    '''
    Method to execute a cql query
    Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
    '''
    session = self.db_session()
    # This line sets up the return type of the query as a dictionary
    session.row_factory = dict_factory
    row_result_as_dict = session.execute(_query).one()
    # return type of this method is a dictionary
    return row_result_as_dict