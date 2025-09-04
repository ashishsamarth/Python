# Import paramiko module : This is the module to handle remote connections
import paramiko
# Import host_conf : This holds the connection params
import host_conf

# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomParamiko:

    def __init__(self, **connection_params: dict):
        '''
        Initialize the class to set the SSH client and set up host addition policy
        Arguments to this method is - **kwargs
        **Key word argument (has three params, user, password and the location of private key)
        '''
        self.ssh = paramiko.SSHClient()
        # setting up the host addition policy is important since, if not defined it will throw
        # paramiko.ssh_exception.SSHException
        # This line adds the hostname to the known_hosts file on the operating system (just once)
        self.host_addition_policy = self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # assign the user provided hostname to initialization method, for reuse across all methods
        self.hostname = connection_params.get('hostname')
        # assign the user provided db_user to initialization method, for reuse across all methods
        self.username = connection_params.get('username')
        # assign the user provided db_user to initialization method, for reuse during connection
        # I have used the absolute path for the key location, one can always use os.path() to manage this
        self.key_filename = connection_params.get('key_filename')

    def host_connect(self):
        '''
        Method to remotely connect to host
        Argument to this method is: Hostname, Username and Location of Private Key for authentication
        '''
        return self.ssh.connect(hostname=self.hostname, username=self.username, key_filename = self.key_filename)

    def execute_command(self, _command):
        '''
        Method to execute specific commands on the connected host
        Argument to this method is: command provided by end user
        Note: read through 'https://stackoverflow.com/questions/42897381' for directory navigation
        paramiko is only good if you run chained commands like 'cd some_path; ls -lrt', non-chained commands do not work very well
        '''
        self.ssh.exec_command(_command)
        return 'command executed successfully'

    def close_connection(self):
        '''
        Method to close the connection of remote host  
        Argument to this method is: None
        '''
        return self.ssh.close()
