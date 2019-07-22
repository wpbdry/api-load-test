class InvalidMethod(Exception):
    def __init__(
        self,
        message="Method must be 'GET'",
        errors=None):
        super().__init__(message)

        if errors:
            self.errors = errors
            