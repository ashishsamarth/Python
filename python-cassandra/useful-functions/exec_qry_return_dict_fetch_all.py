# Method to execute a cql query
# Note the query must have the keyspace included in it, if 'set_keyspace' method was not executed before this
def exec_qry_return_dict_fetch_all(self, _query):
    session = self.db_session()
    # This line sets up the return type of the query as a dictionary
    session.row_factory = dict_factory
    row_result_as_dict = session.execute(_query).all()
    # return type of this method is a list of dictionaries
    return row_result_as_dict