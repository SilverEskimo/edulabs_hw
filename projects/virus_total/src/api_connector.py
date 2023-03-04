import threading

import requests
from virus_total.src.utils.exceptions import *


class ApiConnector:
    def __init__(self, api_key):
        self._api_key = api_key
        self._headers = {
            "x-apikey": self._api_key
        }

    @property
    def api_key(self):
        return self._api_key

    def get_request(self, url, headers: dict | bool = False):
        print(threading.get_ident())
        if headers:
            res = requests.get(url, headers=headers)
        else:
            res = requests.get(url, headers=self._headers)
        if res.status_code < 400:
            return res.json()
        raise ApiCallError(f"The GET API request to {url} "
                           f"failed with the following status code: {res.status_code}")

    def post_request(self, url, body: any, headers: dict | bool = False):
        if headers:
            res = requests.post(url, data=body, headers=headers)
        else:
            res = requests.post(url, data=body, headers=self._headers)
        if res.status_code < 400:
            return res.json()
        raise ApiCallError(f"The POST API request to {url} and {body} "
                           f"failed with the following status code: {res.status_code}")
