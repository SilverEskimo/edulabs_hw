import base64


default_api_key = "5dfb3cbfff6641ca90d2357e6bba52337981fc2627e997d7221e077b0a38b8b7"


def encode_url(url: str):
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")