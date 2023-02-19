# In this exercise you are going to implement the improved version of E1 exercise.
# At the first stage, you need to add to your code the ability to receive multiple names for nationality detection
# (for example, separated by comma). At this stage, you should still run your code in one thread. Try passing 10 names
# and log how much time it takes to get the results for all the names.
import threading
import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed
import climage
import requests



def call_nationalize_api(some_name: str):
    url = f"https://api.nationalize.io/"
    params = {
        "name": f"{some_name}"
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json()
    raise Exception(f"Got an error: status code: {res.status_code}")

def call_country_code_api(cd):

    url = f"https://restcountries.com/v3.1/alpha/{cd.lower()}"
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json())
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")


def call_multiple(name):
    res = call_nationalize_api(name)
    cd = res['country'][0]['country_id']
    call_country_code_api(cd)


if __name__ == '__main__':
    my_name = input("Please enter a list of names separated by comma: ").strip()
    names_list = my_name.split(",")
    fixed_names_list = []
    for name in names_list:
        fixed_names_list.append(name.strip().lower())
    max_prob = 0
    country_codes = []
    try:
        start = time.time()
        with ThreadPoolExecutor(len(fixed_names_list)) as executor:
            futures = []
            for name in fixed_names_list:
                future = executor.submit(call_multiple, name)
                futures.append(future)
        end = time.time()
        print(f"It took: {end - start}")
    except Exception as e:
        print(e)
