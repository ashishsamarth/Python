# Method to get file metadata
# Argument to this method: input filename
def get_file_metadata(self):
    file_metadata = {'File_Name': self.my_filename,
                 'File_Owner_username': getpwuid(os.stat(self.my_filename).st_uid).pw_name,
                 'File_Owner_name': getpwuid(os.stat(self.my_filename).st_uid).pw_gecos,
                 'Created': ctime(os.stat(self.my_filename).st_ctime),
                 'Accessed': ctime(os.stat(self.my_filename).st_atime),
                 'Modified': ctime(os.stat(self.my_filename).st_mtime)
                 }
    return file_metadata