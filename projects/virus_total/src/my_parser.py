import argparse


class MyParser:
    def __init__(self):
        super().__init__()
        self._parser = argparse.ArgumentParser(
            prog="VirusTotal extended scanner",
            description="Allows you to scan a URL by using VirusTotal API",
        )
        self._parser.add_argument('url', help="URL to scan. Separate by comma for more than 1", metavar='URL')
        self._parser.add_argument('-k', '--apiKey', help="API Key to use (optional)", metavar="API Key")
        self._parser.add_argument('-s', '--scan', action='store_true', help="Scan the URL even if exists in cache")
        self._parser.add_argument('-a', '--maxAge', type=int, metavar="Max Age",
                                  help="Provide a custom maximum caching time (default is 6 months")
        self._args = self._parser.parse_args()

    @property
    def args(self):
        return self._args

