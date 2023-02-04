class BestBusEverException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class WrongUserRoleChoice(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class WrongManagerPassword(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class WrongManagerAction(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class WrongPassengerAction(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class WrongLineNumber(BestBusEverException):

    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class WrongScheduledRideFormat(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return self._msg


class RouteExistError(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)

    def __str__(self):
        return self._msg
