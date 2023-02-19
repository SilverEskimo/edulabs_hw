# In this exercise you are going to implement the improved version of E1 exercise.
# At the first stage, you need to add to your code the ability to receive multiple names for nationality detection
# (for example, separated by comma). At this stage, you should still run your code in one thread. Try passing 10 names
# and log how much time it takes to get the results for all the names.
import time

import climage
import requests


def call_nationalize_api(names: list[str]):
    url = f"https://api.nationalize.io/"
    res_list = []
    for n in names:
        params = {
            "name": f"{n}"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            res_list.append(response.json())
        else:
            raise Exception(f"Got an error: status code: {res.status_code}")
    return res_list


def call_country_code_api(some_country_codes: list[str]):
    res_list = []
    for code in some_country_codes:
        url = f"https://restcountries.com/v3.1/alpha/{code.lower()}"
        res = requests.get(url)
        if res.status_code == 200:
            res_list.append(res.json())
        else:
            raise Exception(f"Got an error: status code: {res.status_code}")
    return res_list


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
        nationalize_res = call_nationalize_api(fixed_names_list)
        for res in nationalize_res:
            for item in res["country"]:
                if item["probability"] > max_prob:
                    max_prob = item["probability"]
                    country_codes.append(item["country_id"])
            max_prob = 0

        countries_data = call_country_code_api(country_codes)
        for i, country in enumerate(countries_data):
            print(f"The country with the highest probability for the name {fixed_names_list[i].title()}: \n"
                  f"Country Code: {country_codes[i].upper()}\nCountry Name: {country[0]['name']['official']}\n"
                  f"Continent: {country[0]['continents'][0]}")
            # get_and_save_flag_image(country_data[0]["flags"]["png"])
        end = time.time()
        print(f"It took: {end - start}")
    except Exception as e:
        print(e)
