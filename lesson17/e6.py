# Write a program that receives a number of seconds from a user and counts down this amount of seconds in
# resolution of 0.1 second by printing the amount of time left.
import time
import requests
from concurrent.futures import ThreadPoolExecutor, Future, as_completed


def get_kanye_quote():
    url = "https://api.kanye.rest/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json()["quote"])
    else:
        print(response.status_code)


def count_down_ms(seconds: str):
    print(f"Starting countdown from {seconds} seconds")
    count = 0
    try:
        seconds_float = float(seconds)
        while seconds_float > 0:
            secs_to_print = "{:.1f}".format(seconds_float)
            print(secs_to_print)
            seconds_float -= 0.1
            count += 1
            if count == 10:
                count = 0
                with ThreadPoolExecutor(1) as executor:
                    executor.submit(get_kanye_quote)
            time.sleep(0.1)
        print("Fire!")
    except TypeError:
        raise TypeError("Seconds must be float")


if __name__ == '__main__':
    seconds_str = input("Please enter the amount of seconds to countdown from: ").strip()
    while True:
        try:
            count_down_ms(seconds_str)
            break
        except TypeError as e:
            print(e)

