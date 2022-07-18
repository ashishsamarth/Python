# Method to create a cursor on the connected database
# Argument to this method: None
def db_cursor_open(self):
    print('Cursor is manually opened, always remember to close it by calling db_cursor_close')
    return self.db_auto_connect.cursor()