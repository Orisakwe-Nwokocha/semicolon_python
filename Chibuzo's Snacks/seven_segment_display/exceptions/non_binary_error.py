class NonBinaryNumberError(Exception):
    def __init__(self, message):
        super(NonBinaryNumberError, self).__init__(message)
