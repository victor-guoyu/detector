class InvalidArgument(Exception):
    pass


class InvalidFileInput(Exception):
    def __init__(self, message):
        self.message = message

class InvalidTupleSize(Exception):
    pass