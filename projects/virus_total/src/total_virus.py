from virus_total.src.utils import utils
from concurrent.futures import ThreadPoolExecutor, as_completed
from virus_total.src.api_connector import ApiConnector


class TVscanner:
    def __init__(self, api_key=None):
        self._base_url = "https://www.virustotal.com/api/v3"
        self._api_connector = ApiConnector(api_key) if api_key else ApiConnector(utils.default_api_key)
        self._cache = {}

    def scan_urls(self, urls: list):
        futures = []
        res_list = []
        with ThreadPoolExecutor(len(urls)) as executor:
            for url in urls:
                future = executor.submit(
                    self._api_connector.post_request, self._base_url, url)
                futures.append(future)
                for future in as_completed(futures):
                    res_list.append(future.result())
        return res_list

    def get_urls_reputation(self, urls: list):
        futures = []
        res_list = []
        with ThreadPoolExecutor(len(urls)) as executor:
            for url in urls:
                encoded_url = utils.encode_url(url)
                future = executor.submit(self._api_connector.get_request, f"{self._base_url}/urls/{encoded_url}")
                futures.append(future)
            for future in as_completed(futures):
                res_list.append(future.result())
        return res_list

    def check_if_cached(self):
        return self._cache
