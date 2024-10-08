# Import paramiko module : This is the module to handle remote connections
import paramiko
# Import host_conf : This holds the connection params
import host_conf


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomParamiko:

    # Initialize the class to set the SSH client and set up host addition policy
    # Arguments to this method is - **kwargs
    # **Key word argument (has three params, user, password and the location of private key)
    def __init__(self, **connection_params):
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
        self.key_filename = connection_params.get('key_filename')