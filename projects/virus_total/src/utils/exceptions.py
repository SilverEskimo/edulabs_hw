class ApiCallError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ReputationDoesNotExist(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidAPIKey(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class RateLimitExceeded(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UrlNotFound(Exception):
    def __init__(self, msg, url):
        self._msg = msg
        self._url = url
        super().__init__()

    @property
    def url(self):
        return self._url

    @property
    def msg(self):
        return self._msg


class UrlIsNotCached(UrlNotFound):
    def __init__(self, msg, url):
        super().__init__(msg, url)


class IllegalURL(UrlNotFound):
    def __init__(self, msg, url):
        super().__init__(msg, url)
