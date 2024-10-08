# Method to generate a random password
# Import the string package
import string
# From the random module import the choice method
from random import choice
# Set the default length of password as 20, if its not provided while calling this method
def generate_rdm_pass(length=20):
    # randomly select 20 characters from a combination of letters, digits and punctuations
    return ''.join(choice(string.ascii_letters + string.digits + string.punctuation) for i in range (length))
    