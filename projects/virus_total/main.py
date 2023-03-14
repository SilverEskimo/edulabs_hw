import pprint
from src.my_parser import MyParser
from src.virus_total import VTscanner


if __name__ == '__main__':
    args = MyParser().args
    vt = VTscanner(args.apiKey) if args.apiKey else VTscanner()
    urls = args.url.split(",")

    vt.check_api_key()
    print("Valid API Key")
    vt.check_valid_urls(urls)
    print("Valid URLs")

    if args.scan:
        res = vt.scan_urls(urls)
        print("Your results:")
        pprint.pprint(res)
    else:
        result = []
        max_age = args.maxAge if args.maxAge else 180
        aged_urls = vt.check_if_aged(urls, max_age)
        non_aged_urls = set(urls).difference(set(aged_urls))
        if aged_urls:
            print("Some of the urls are over the max age")
            result += vt.scan_urls(aged_urls)
            if non_aged_urls:
                result += vt.get_analysis_report(list(non_aged_urls))
            print("Your results:")
            pprint.pprint(result)
        else:
            print("No max aged urls")
            res = vt.get_analysis_report(urls)
            print("Your results:")
            pprint.pprint(res)
