# Method to check if a string is a palindrome
@staticmethod
# Argument to this method: string
def str_is_palindrome(_my_string):
    reversed_string = _my_string[::-1]
    if _my_string == reversed_string:
        return True
    return False
