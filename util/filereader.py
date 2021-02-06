class FileReader:
    """FileReader utility class; handles reading in file input line by line and parsing out to requested formats."""

    def __init__(self, path, split=True):
        if split:
            self.data = open(path, "r").read().split("\n")
        else:
            self.data = open(path, "r").read()

    def parseInt(self):
        return [int(i) for i in self.data]
