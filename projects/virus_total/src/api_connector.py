import requests
from .utils import utils
from .utils.exceptions import *


class ApiConnector:
    def __init__(self, api_key):
        self._base_url = "https://www.virustotal.com/api/v3/urls"
        self._api_key = api_key
        self._headers = {
            "x-apikey": self._api_key
        }

    @property
    def api_key(self):
        return self._api_key

    def get_analysis_request(self, url):
        encoded_url = utils.encode_url(url)
        res = ApiConnector._get_request("/".join([self._base_url, encoded_url]), self._headers)
        if res.status_code < 400:
            return res.json()
        if res.status_code == 401:
            raise InvalidAPIKey("Invalid API key")
        if res.status_code == 404:
            raise UrlNotFound("Not Found", url)
        if res.status_code == 429:
            raise RateLimitExceeded("You have exceeded the rate limit")
        raise ApiCallError(f"The GET API request to {url} "
                           f"failed with the following status code: {res.status_code}")

    def post_scan_request(self, body: any):
        res = ApiConnector._post_request(self._base_url, body, self._headers)
        if res.status_code < 400:
            return res.json()
        if res.status_code == 429:
            raise RateLimitExceeded("You have exceeded the rate limit")
        raise ApiCallError(f"The POST Scan API request with body: {body} "
                           f"failed with the following status code: {res.status_code}")

    @staticmethod
    def _post_request(url, body, headers):
        return requests.post(url, data=body, headers=headers)

    @staticmethod
    def _get_request(url, headers):
        return requests.get(url, headers=headers)
