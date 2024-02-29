class NonDigitNumberError(Exception):
    def __init__(self, message):
        super(NonDigitNumberError, self).__init__(message)
