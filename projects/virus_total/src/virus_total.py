import pdb
from time import sleep

from .utils import utils
from .utils.exceptions import *
from .api_connector import ApiConnector
from concurrent.futures import ThreadPoolExecutor, as_completed


class VTscanner:
    def __init__(self, api_key=None):
        self._base_url = "https://www.virustotal.com/api/v3/urls"
        self._api_connector = ApiConnector(api_key) if api_key else ApiConnector(utils.default_api_key)
        self._cache = {}

    def scan_urls(self, urls: list):
        futures = []
        res_list = []
        with ThreadPoolExecutor(len(urls)) as executor:
            for url in urls:
                body = {'url': {url}}
                future = executor.submit(self._api_connector.post_request, self._base_url, body)
                futures.append(future)
                for future in as_completed(futures):
                    try:
                        res_list.append(future.result())
                    except ApiCallError as e:
                        print(f"Error: {e}")
        return res_list

    def get_urls_reputation(self, urls: list):
        futures = []
        res_list = []
        with ThreadPoolExecutor(len(urls)) as executor:
            for url in urls:
                encoded_url = utils.encode_url(url)
                future = executor.submit(self._api_connector.get_request, f"{self._base_url}/{encoded_url}")
                futures.append(future)
            for future in as_completed(futures):
                try:
                    if type(future.result()) == str:
                        print(f"URL does not exist in VT: {url}, need to rescan...")
                        print("Future:", future.result())
                    else:
                        res_list.append(future.result())
                except ApiCallError as e:
                    print(f"Error: {e}")
        return res_list

    def rescan_non_existing(self, urls):
        self.scan_urls(urls)
        sleep(1)
        return self.get_urls_reputation(urls)

    def check_if_cached(self):
        pass

    def save_in_cache(self, urls):
        pass



