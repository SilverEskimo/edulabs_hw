# Implement a function that does not receive any argument, and returns the amount of days
# left until the end of the current year.
import datetime

if __name__ == '__main__':

    def days_until_end_of_year():
        today = datetime.datetime.now()
        end_of_year = datetime.datetime(year=int(today.strftime("%Y")), month=12, day=31)
        return str(end_of_year - today)[:str(end_of_year - today).index(",")]

    print(days_until_end_of_year())