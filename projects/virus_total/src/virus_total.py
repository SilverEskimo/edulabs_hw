import json
import os.path
from time import sleep
from .utils import utils
from threading import Lock
from .utils.exceptions import *
from .api_connector import ApiConnector
from concurrent.futures import ThreadPoolExecutor, as_completed


class VTscanner:
    def __init__(self, api_key=None):
        self._api_connector = ApiConnector(api_key) if api_key else ApiConnector(utils.default_api_key)
        self._url_cache: dict = {}
        self._data_cache: dict = {}
        self._cache_lock = Lock()

    '''Scan a single URL
    Args:
        url - URL to scan
    Returns:
        VirusTotal scan URL object:
        https://developers.virustotal.com/reference/scan-url
    '''

    def _scan_url(self, url: str) -> dict:
        body = {'url': {url}}
        try:
            return self._api_connector.post_scan_request(body)
        except RateLimitExceeded as e:
            raise RateLimitExceeded(e)
        except ApiCallError as e:
            raise ApiCallError(e)

    '''Get analysis report for a single URL
    Args:
        url - a URL to get the analysis for
    Returns:
        VirusTotal URL object
        https://developers.virustotal.com/reference/url-info
    '''

    def _get_analysis_report(self, url: str) -> dict:
        try:
            return self._api_connector.get_analysis_request(url)
        except UrlNotFound as e:
            raise UrlNotFound(e.msg, e.url)
        except RateLimitExceeded as e:
            raise RateLimitExceeded(e)
        except InvalidAPIKey as e:
            raise InvalidAPIKey(e)
        except ApiCallError as e:
            raise ApiCallError(e)

    '''Wait for analysis result until it gets scanned and returns result
    Args:
        urls - List of URLs pending for analysis result
    Returns:
        List of analysis results
    '''

    def _wait_for_result(self, urls: list) -> list[dict]:
        count = 0
        print("Waiting for the analysis result. Kindly note that this might take up to a few minutes.")
        while True:
            sleep(10)
            res = self.get_analysis_report(urls, first_scan=False)
            analysis_results = []
            for r in res:
                if r.get('data', {}).get('attributes', {}).get('last_analysis_date', {}):
                    analysis_results.append(r)
                    self.cache_url(r["data"]["attributes"]["url"][:-1], r)
            if len(analysis_results) == len(urls):
                break
            if count % 2 == 0:
                print("I am still checking. No worries!")
            elif count % 3 == 0:
                print("Yep, still here...it takes some time today")
            count += 1
        return analysis_results

    '''Check if a specific URL is cached
    Args:
        url - url to check in cache
    Returns:
        Analysis result
    '''

    def _check_if_cached(self, url: str) -> dict:
        with self._cache_lock:
            if not os.path.exists("urls.json"):
                with open("urls.json", "w") as f:
                    json.dump({}, f)
            else:
                with open("urls.json", 'r') as f:
                    self._url_cache = json.load(f)
                    for key, value in self._url_cache.items():
                        if url == key:
                            with open(f"{value}.json", 'r') as df:
                                self._data_cache = json.load(df)
                                for k, v in self._data_cache.items():
                                    if url == k:
                                        return v
            raise UrlIsNotCached("Not cached", url)

    '''Cache a specific url
    Args:
        url - URL to cache
        result - analysis result to cache
    '''
    def cache_url(self, url: str, result: dict) -> None:
        with self._cache_lock:
            with open("urls.json", "r+") as f:
                self._url_cache = json.load(f)
                file_name = utils.search_file_name(url)
                self._url_cache[url] = file_name
                if not os.path.exists(f"{file_name}.json"):
                    with open(f"{file_name}.json", "w") as data_file:
                        json.dump({url: result}, data_file)
                else:
                    with open(f"{file_name}.json", "r+") as data_file:
                        self._data_cache = json.load(data_file)
                        self._data_cache[url] = result
                        data_file.seek(0)
                        json.dump(self._data_cache, data_file)
                print(f"Successfully cached {url}")
                self._url_cache[url] = file_name
                f.seek(0)
                json.dump(self._url_cache, f)

    ''' Get an analysis report including checking cached URLs and rescanning for non existing
    Args:
        urls - List of URLs to get the results for
        first_scan - Boolean flag for internal usage
    Returns:
        List of analysis results
    '''

    def get_analysis_report(self, urls: list, first_scan=True) -> list[dict]:
        results = []
        check_cached = self.check_if_cached(urls)
        non_cached_urls = check_cached["non_cached"]
        results += check_cached["cached"]
        if non_cached_urls:
            futures = []
            urls_to_scan = []
            workers = len(non_cached_urls)
            with ThreadPoolExecutor(workers) as executor:
                for url in non_cached_urls:
                    future = executor.submit(self._get_analysis_report, url)
                    futures.append(future)
            for future in as_completed(futures):
                try:
                    res = future.result()
                    results.append(res)
                    url_to_cache = res.get('data').get('attributes').get('url')[:-1]
                    full_result = res.get('data', {}).get('attributes', {}).get('last_analysis_date', {})
                    if full_result:
                        self.cache_url(url_to_cache, res)
                except UrlNotFound as e:
                    urls_to_scan.append(e.url)
                except (ApiCallError, RateLimitExceeded) as e:
                    raise Exception(e)
            if urls_to_scan and first_scan:
                try:
                    results += self.scan_urls(urls_to_scan)
                except (ApiCallError, RateLimitExceeded) as e:
                    print(e)
                    exit(1)
        return results

    ''' Scan URLs
    Args:
        urls_to_scan - List of URLs to submit for scanning
    Returns:
        List of analysis results
    '''
    def scan_urls(self, urls_to_scan: list) -> list[dict]:
        print(f"Going to scan {urls_to_scan}")
        workers = len(urls_to_scan)
        with ThreadPoolExecutor(workers) as executor:
            for url in urls_to_scan:
                try:
                    executor.submit(self._scan_url, url)
                except ApiCallError as e:
                    raise ApiCallError(e)
                except RateLimitExceeded as e:
                    raise RateLimitExceeded(e)
        return self._wait_for_result(urls_to_scan)

    ''' Check if URLs are cached
    Args:
        urls - List of URLs to check
    Returns:
        Dict with cached and non cached URLs
    '''
    def check_if_cached(self, urls: list) -> dict[str: list]:
        futures = []
        cached_urls = []
        non_cached_urls = []
        with ThreadPoolExecutor(len(urls)) as executor:
            for url in urls:
                future = executor.submit(self._check_if_cached, url)
                futures.append(future)
        for future in as_completed(futures):
            try:
                res = future.result()
                cached_urls.append(res)
            except UrlIsNotCached as e:
                non_cached_urls.append(e.url)
        return {
            "non_cached": non_cached_urls,
            "cached": cached_urls
        }

    ''' Check if API key is valid
    Returns:
        Analysis result for google
    '''
    def check_api_key(self) -> dict:
        try:
            return self._get_analysis_report("https://google.com")
        except InvalidAPIKey as e:
            print(e)
            exit(1)

    ''' Check if the provided URLs are valid, i.e don't start with special characters
    Args:
        urls - List of URLs to validate
    '''

    @staticmethod
    def check_valid_urls(urls: list) -> None:
        for url in urls:
            try:
                utils.search_file_name(url)
            except IllegalURL as e:
                print(e.msg, e.url)
                exit(1)

    ''' Check if URLs are over the default or custom max age
    Args:
        urls - List of URLs to check
        max_age - Max age (default is 180 days)
    Returns:
        List of URLs over the max age
    '''
    def check_if_aged(self, urls: list, max_age: int) -> list[str]:
        futures = []
        aged_urls = []
        workers = len(urls)
        with ThreadPoolExecutor(workers) as executor:
            for url in urls:
                future = executor.submit(self._check_if_cached, url)
                futures.append(future)
        for future in as_completed(futures):
            try:
                res = future.result()
                last_scan = res['data']['attributes']['last_analysis_date']
                if utils.check_if_aged(last_scan, max_age):
                    aged_urls.append(res['data']['attributes']['url'][:-1])
            except UrlIsNotCached:
                pass
        return aged_urls
