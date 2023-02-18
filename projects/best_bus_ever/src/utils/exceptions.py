class BestBusEverException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class WrongUserRoleChoice(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)


class WrongManagerPassword(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)


class WrongManagerAction(BestBusEverException):
    def __init__(self, msg: str):
        super().__init__(msg)


class WrongPassengerAction(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongLineNumber(BestBusEverException):

    def __init__(self, msg):
        super().__init__(msg)


class WrongScheduledRideFormat(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class RouteExistError(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongUpdateRange(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongTimeFormat(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongSearchTerm(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongRideId(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)


class WrongDelayFormat(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)

class WrongDateFomat(BestBusEverException):
    def __init__(self, msg):
        super().__init__(msg)