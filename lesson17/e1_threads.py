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


def call_country_code_api(future: Future):
    param = future.result()
    print(param)
    url = f"https://restcountries.com/v3.1/alpha/{param['country'][0]['country_id'].lower()}"
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json())
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")


# def get_and_save_flag_image(image_url):
#     image_data_res = requests.get(image_url)
#     if image_data_res.status_code == 200:
#         with open('flag.png', "wb") as f:
#             f.write(image_data_res.content)
#         print(climage.convert('flag.png', width=40))
#     else:
#         raise Exception(f"Got an error: status code: {image_data_res.status_code}")


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
                future = executor.submit(call_nationalize_api, name)
                futures.append(future)

            for future in as_completed(futures):
                call_country_code_api(future)
        end = time.time()
        print(f"It took: {end - start}")
    except Exception as e:
        print(e)
