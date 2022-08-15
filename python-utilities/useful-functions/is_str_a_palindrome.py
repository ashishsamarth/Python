# Method to check if a string is a palindrome
# Argument to this method: string
def is_str_a_palindrome(_inp_str):
    reversed_string = _inp_str[::-1]
    return True if _inp_str == reversed_string else False