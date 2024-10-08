# Method to fetch specific number of rows of sql output
# Argument to this method is: SQL Query or Variable containing the SQL query
# Note: Order of the result is driven by sql query
def db_execute_sql_fetch_specific_num_of_rows_as_dict(self, _sql_query_or_sql_variable, _num_of_rows):
    with self.db_auto_connect.cursor() as cursor:
        '''
        If you are fetching a fixed number of rows, start your tuning by setting arraysize to the number of expected 
        rows, and set prefetchrows to one greater than this value. (Adding one removes the need for a round-trip to 
        check for end-of-fetch)
        '''
        cursor.arraysize = _num_of_rows
        cursor.prefetchrows = _num_of_rows + 1
        # Execute the SQL Query or Variable containing the SQL query
        execute = cursor.execute(_sql_query_or_sql_variable)
        # Fetch the column names from cursor.description using list comprehension
        # 'description' attribute on a cursor holds the column names for the tables in question
        columns = [row[0] for row in execute.description]
        '''
        Special Note:Cursor.rowfactory The rowfactory attribute of the Cursor object defines the method that will be
          called when retrieving the record. This attribute produces tuples by default. By overwriting this movement,
           it is possible to change the format of the record to another form.
        '''
        # Here we are changing the form from tuples to a dictionary
        execute.rowfactory = lambda *args: dict(zip(columns, args))
        # Fetch only specific number of rows from the cursor in to results
        results = execute.fetchmany(numRows=_num_of_rows)
    # return type of this method is a dictionary
    return results