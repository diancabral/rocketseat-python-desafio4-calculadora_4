class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = 422
        self.message = message
        self.name = 'UnprocessableEntity'
