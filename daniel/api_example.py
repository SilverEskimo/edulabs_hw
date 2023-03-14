from pprint import pprint

import requests


if __name__ == '__main__':
    # res = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    # print(res.status_code)
    # pprint(res.json())
    #
    # res2 = requests.get(f"https://deckofcardsapi.com/api/deck/{res.json()['deck_id']}/draw/?count=1")
    # print(res2.status_code)
    # pprint(res2.json())
    #
    # print("Going to get the image:")
    # res3 = requests.get(f"{res2.json()['cards'][0]['image']}")
    # print(res3.status_code)
    # pprint(res3.content)
    #
    # with open("demo.png", 'wb') as f:
    #     f.write(res3.content)
