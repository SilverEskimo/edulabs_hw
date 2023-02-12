# Implement a function that gets a list of strings that represent dates in format dd-mm-yyyy.
# Use map() and filter() to filter from this list all the dates that are Fridays and Saturdays.
# Your function should return datetime objects.
# Test with the following list: ['12-12-2021', '18-12-2021', '19-12-2021]
# Write 2 additional unit tests to test your implementation
import datetime


def my_func(dates: list[str]):
    mapped = map(lambda date: datetime.datetime.strptime(date, "%d-%m-%Y"), dates)
    return filter(lambda date: date.weekday() not in [4, 5], mapped)


if __name__ == '__main__':
    my_dates = ['12-12-2021', '18-12-2021', '19-12-2021']
    print(list(my_func(my_dates)))
