# Import paramiko module : This is the module to handle remote connections
import paramiko
# Import paramiko_conf : This holds the connection params
import paramiko_conf


# Class definitions should use CamelCase convention based on pep-8 guidelines
class ManageCassandra:
    
    def __init__(self, **connection_params):
        '''
        Initialize the class to set the SSH client and set up host addition policy
        Arguments to this method is - **kwargs
        **Key word argument (has three params, user, password and the location of private key)
        '''
        self.ssh = paramiko.SSHClient()
        # setting up the host addition policy is important since, if not defined it will throw paramiko.ssh_exception.SSHException
        # This line adds the hostname to the known_hosts file on the operating system (just once)
        self.host_addition_policy = self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # assign the user provided hostname to initialization method, for reuse across all methods
        self.hostname = connection_params.get('hostname')
        # assign the user provided db_user to initialization method, for reuse across all methods
        self.username = connection_params.get('username')
        # assign the user provided db_user to initialization method, for reuse during connection
        self.key_filename = connection_params.get('key_filename')

    def host_connect(self):
        '''
        Method to remotely connect to host
        Argument to this method is: Hostname, Username and Location of Private Key for authentication
        '''
        remote_connect = self.ssh.connect(hostname=self.hostname, username=self.username, key_filename = self.key_filename)
        return remote_connect
    
    def execute_command(self, _command):
        '''
        Method to execute specific commands on the connected host
        Argument to this method is: command provided by end user
        '''
        stdin, stdout, stderr = self.ssh.exec_command(_command)
        # standard output from the command execution is sent to a variable
        command_output = stdout.read()
        # command output is returned to the code execution
        return command_output
    
    def start_dse_cassandra(self, _dir_path):
        '''
        Method to start DSE-Cassandra on remote host
        Since the Cassandra DB is on a cloud server, managing it from location machine needs SSH client
        Hence 'execute_method()' of 'paramiko' module is used, even though the focus is to manage Cassandra and not the remote server
        '''
        # Build the chained command to navigate to the directory and execute the required command
        start_cassandra = f'cd {_dir_path}' + ';' + './dse cassandra'
        # execute the command
        # This command will navigate to the cassandra_home directory and start Datastax-Enterprise version of Cassandra
        self.execute_command(start_cassandra)
        # The return type of this method is None
    
    def stop_dse_cassandra(self, _dir_path):
        '''
        Method to stop DSE-Cassandra on remote host
        Since the Cassandra DB is on a cloud server, managing it from location machine needs SSH client
        Hence 'execute_method()' of 'paramiko' module is used, even though the focus is to manage Cassandra and not the remote server
        '''
        # Build the chained command to navigate to the directory and execute the required command
        # This command will navigate to the cassandra_home directory and stop Datastax-Enterprise version of Cassandra
        stop_cassandra = f'cd {_dir_path}' + ';' + './dse cassandra-stop'
        self.execute_command(stop_cassandra)
        # The return type of this method is None
    
    def cassandra_status(self, _dir_path):
        '''
        Method to check the status of Cassandra Nodes on remote host
        Since the Cassandra DB is on a cloud server, managing it from location machine needs SSH client
        Hence 'execute_method()' of 'paramiko' module is used, even though the focus is to manage Cassandra and not the remote server
        '''
        # Build the chained command to navigate to the directory and execute the required command
        # This command will navigate to the cassandra_home directory and check the node status of Datastax-Enterprise version of Cassandra
        check_cassandra = f'cd {_dir_path}' + ';' + './nodetool status'
        self.execute_command = (check_cassandra)
        # The return type of this method is None
    
    def close_connection(self):
        '''
        Method to close the connection of remote host
        Argument to this method is: None
        '''
        self.ssh.close()
