import base64
import datetime
from .exceptions import *

default_api_key = "27ac9da3c1fcebd7905695f41919c448bec2aea95da31e23e33b13cf8e709be8"

file_mapping = {
    "urls1": "abcdefg",
    "urls2": "hijklmn",
    "urls3": "opqrst",
    "urls4": "uvwxyz",
    "urls5": "0123456789"
}


def encode_url(url: str):
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")


def format_url(url: str):
    if url.startswith('http://'):
        return url.replace('http://', "")
    if url.startswith('https://'):
        return url.replace('https://', "")
    return url


def search_file_name(url: str):
    formatted_url = format_url(url)
    for key, value in file_mapping.items():
        if formatted_url[0] in value:
            return key
    raise IllegalURL("Illegal url (starts with non alphanumeric):", url)


def check_if_aged(last_scan, max_age):
    aged_epoch = (datetime.datetime.today() - datetime.timedelta(max_age)).strftime('%s')
    return last_scan < int(aged_epoch)
