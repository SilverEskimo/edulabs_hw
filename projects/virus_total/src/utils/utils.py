import base64

default_api_key = "5dfb3cbfff6641ca90d2357e6bba52337981fc2627e997d7221e077b0a38b8b7"
file_mapping = {
    "urls1": "abcdefg",
    "urls2": "ghijkl",
    "urls3": "mnopqr",
    "urls4": "stuvwxyz"
}


def encode_url(url: str):
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")



