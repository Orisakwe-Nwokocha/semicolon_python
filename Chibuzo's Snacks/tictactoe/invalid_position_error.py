class InvalidPositionError(Exception):
    def __init__(self, message):
        super(InvalidPositionError, self).__init__(message)
