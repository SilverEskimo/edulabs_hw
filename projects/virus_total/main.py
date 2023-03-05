import datetime
import string

from src.my_parser import MyParser
from src.virus_total import VTscanner


if __name__ == '__main__':
    args = MyParser().args
    vt = VTscanner(args.apiKey) if args.apiKey else VTscanner()
    urls = args.url.split(",")
    print(string.ascii_lowercase[:7])
    if args.scan:
        print(f"Scanning {urls}")
        vt.scan_urls(urls)
        print("Done scanning, getting the result")
        res = vt.get_urls_reputation(urls)
        last_scanned = res[0]['data']['attributes']['last_analysis_date']
        print("Last scan:", datetime.datetime.fromtimestamp(last_scanned).strftime('%Y-%m-%d %H:%M:%S'))

    else:
        res = vt.get_urls_reputation(urls)
        print(res)



