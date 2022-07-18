# Method to manually close the cursor
# Argument to this method: None
def db_cursor_close(self):
    return self.db_cursor_open().close()