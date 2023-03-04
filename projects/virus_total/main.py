from src.total_virus import TVscanner


if __name__ == '__main__':
    url_scanner = TVscanner()
    res = url_scanner.get_urls_reputation(
        [
            "https://google.com",
            "https://amazon.com",
            "https://facebook.com"
        ]
    )


