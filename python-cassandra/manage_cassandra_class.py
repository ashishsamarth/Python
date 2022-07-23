# Import paramiko module : This is the module to handle remote connections
import paramiko
# Import paramiko_conf : This holds the connection params
import paramiko_conf


# Class definitions should use CamelCase convention based on pep-8 guidelines
class ManageCassandra:
    # Initialize the class to set the SSH client and set up host addition policy
    # Arguments to this method is - **kwargs
    # **Key word argument (has three params, user, password and the location of private key)