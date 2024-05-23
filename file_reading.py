class file_reading:
    def __init__(self, filename):
        self.file_handle = open(filename, "rb")

        if not self.file_handle.seekable():
            raise Exception("Input must be seekable!")

    def close(self):
        self.file_handle.close()

    def read(self):
        line = self.file_handle.readlines()
        return line
