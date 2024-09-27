# Method to read the file, default num of lines is 0
def file_read_mode_read_line(self, num_of_lines=0):
    # open the filename captured during initialization in read mode
    with open(self.my_filename, 'r') as read_mode:
        # The default value of argument num_of_lines is zero, so following line of code will only read one line
        single_line = read_mode.readline()
        # If the value for # of lines is provided, it will be passed to the code and that many lines will be read
        if num_of_lines > 0:
            multilines = read_mode.readlines(num_of_lines)
            # _ is a temp operator which will not be used outside the context of for loop
            for _ in multilines:
                print(_)
        else:
            print(single_line)