import requests
import climage

def call_nationalize_api(name: str):
    url = f"https://api.nationalize.io/"
    params = {
        "name": f"{name}"
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")

# "flags":{"png":"https://flagcdn.com/w320/gh.png"
def call_country_code_api(country_code: str):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.lower()}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Got an error: status code: {res.status_code}")


def get_and_save_flag_image(image_url):
    image_data_res = requests.get(image_url)
    if image_data_res.status_code == 200:
        with open('flag.png', "wb") as f:
            f.write(image_data_res.content)
        print(climage.convert('flag.png', width=40))
    else:
        raise Exception(f"Got an error: status code: {image_data_res.status_code}")


if __name__ == '__main__':
    my_name = input("Please enter your name: ").strip().lower()
    max_prob = 0
    country_code = ""
    try:
        nationalize_res = call_nationalize_api(my_name)
        for item in nationalize_res["country"]:
            if item["probability"] > max_prob:
                max_prob = item["probability"]
                country_code = item["country_id"]
        country_data = call_country_code_api(country_code)
        country_name = country_data[0]["name"]
        print(f"The country with the highest probability for the name {my_name.title()}: \n"
              f"Country Code: {country_code.upper()}\nCountry Name: {country_name['official']}\nContinent: "
              f"{country_data[0]['continents'][0]}")
        get_and_save_flag_image(country_data[0]["flags"]["png"])
    except Exception as e:
        print(e)

