# Implement a function that receives a day of the week represented as a 3-char string (‘sun’, ‘mon’, tue’, …),
# and returns how many of these weekdays are left until the end of the current month.
import datetime

DAYS_OF_WEEK = {
    "sun": 6,
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
}

if __name__ == '__main__':
    def how_many_left(week_day: str) -> int:
        today = datetime.datetime.today()
        current_month = int(today.strftime("%-m"))
        month = current_month
        count = 0
        if today.weekday() == DAYS_OF_WEEK[week_day.lower()]:
            count -= 1
        while month == current_month:
            if today.weekday() == DAYS_OF_WEEK[week_day.lower()]:
                count += 1
            today += datetime.timedelta(1)
            month = int(today.strftime("%-m"))
        if count == -1:
            return 0
        return count

    print(how_many_left("sat"))
