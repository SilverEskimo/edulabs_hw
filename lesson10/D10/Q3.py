# Implement a function that receives a date in format like the following:
# Mon, Dec 19, 2022 10:00 PM
# and returns the amount of time left until the provided date.
# The function should return a timedelta object.
import datetime


if __name__ == '__main__':
    def timedelta_until_date(some_date: str) -> datetime.timedelta:
        target_date = datetime.datetime.strptime(some_date, "%a, %b %d, %Y %I:%M %p")
        return target_date - datetime.datetime.now()

    print(timedelta_until_date("Mon, Dec 19, 2023 10:00 PM"))