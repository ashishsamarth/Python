# Dictionary to hold  the host and port information
db_config = {'host': '192.168.1.22',
             'port': 27017}

# Dictionary to hold credentials for Mongo DB Admin
priv_user_conf = {'username': 'mongo_db_admin',
                  'password': 'password',
                  'authSource': 'admin',
                  'authMechanism': 'SCRAM-SHA-256'}

# Dictionary to hold credentials for Application User
python_api_user_conf = {'username': 'python_api',
                        'password': 'password',
                        'authSource': 'development',
                        'authMechanism': 'SCRAM-SHA-256'}

# Dictionary to hold **kwargs for Mongo DB Admin
# This dictionary is passed to __init__ during class initialization
priv_user_connect = {'host': db_config['host'],
                     'port': db_config['port'],
                     'username': priv_user_conf['username'],
                     'password': priv_user_conf['password'],
                     'authSource': priv_user_conf['authSource'],
                     'authMechanism': priv_user_conf['authMechanism']}

# Dictionary to hold **kwargs for Application User
# This dictionary is passed to __init__ during class initialization
python_api_connect = {'host': db_config['host'],
                      'port': db_config['port'],
                      'username': python_api_user_conf['username'],
                      'password': python_api_user_conf['password'],
                      'authSource': python_api_user_conf['authSource'],
                      'authMechanism': python_api_user_conf['authMechanism']}