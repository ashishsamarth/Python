# Method to check if given string is empty or not
@staticmethod
# Argument to this method: string
def chk_if_string_empty(_my_string: str):
    if not _my_string:
        return f'Given String is empty'
    return f'Given String is not empty'
