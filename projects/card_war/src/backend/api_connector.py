import requests


class ApiConnector:
    @staticmethod
    def get_call(url, headers=False):
        if headers:
            return requests.request("GET", url, headers=headers)
        return requests.request("GET", url)

