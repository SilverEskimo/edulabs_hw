class ApiCallError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ReputationDoesNotExist(Exception):
    def __init__(self, msg):
        super().__init__()