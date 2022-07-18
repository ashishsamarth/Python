import cx_Oracle

ora_client_config = {'orcl_client_path': r'C:\oracle\instantclient_21_3'}

db_config = {'host': '192.168.0.22',
             'port': 1521,
             'service_name': 'ORCLPDB'}

python_api_user_config = {'user': 'python_api',
                          'password': 'python_api',
                          'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name']}

soda_user_config = {'user': 'sodauser',
                    'password': 'sodauser',
                    'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name']}

# Comment Specific only for privileged connection
'''
Do not convert value of mode to a string as 'cx_Oracle.SYSDBA', since cx_Oracle.SYSDBA eventually
refers to mode = 2. if its converted to string you will continue to see
TypeError: an integer is required (got type str) while attempting to connect
'''
privileged_user = {'user': 'SYS',
                   'password': 'Black0ps',
                   'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name'],
                   'mode': cx_Oracle.SYSDBA}
