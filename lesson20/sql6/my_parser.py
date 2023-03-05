import argparse


class MyParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            prog="IMDB app",
            description="Check if movie exists and get all the movies with rating >= input",
        )
        self._parser.add_argument('-n', '--name', help="Movie name to search", metavar='Movie Name')
        self._parser.add_argument('-r', '--rating', help="Minimum rating to search", metavar="Rating")
        self._args = self._parser.parse_args()

    @property
    def args(self):
        return self._args

