import requests


def genderize(name):
    response = requests.get("https://api.genderize.io/",
                            params={ "name": { name } })

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Got error from the API: Code - {response.status_code}")

if __name__ == '__main__':
    # response = requests.get("https://api.kanye.rest/")
    # if response.status_code == 200:
    #     print(response.json()["quote"])
    # else:
    #     print(f"Got error from the API: Code - {response.status_code}")
    name = input("Please enter a name: ")
    genderize(name)

