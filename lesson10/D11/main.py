import datetime
from lesson10.D11.CountryCalendar import *

if __name__ == '__main__':
    my_calendar = CountryCalendar(
        "Israel",
        [6, 0, 1, 2, 3],
        2023,
        [
            datetime.datetime.now(),
            datetime.datetime(year=2022, month=10, day=13)
        ]
    )
    from_date = datetime.datetime(year=2022, month=10, day=10)
    to_date = datetime.datetime(year=2022, month=10, day=23)
    print("Working days:", my_calendar.total_working_days(from_date, to_date))
    print("Vacation Days:", my_calendar.total_vacation_days(from_date, to_date))
    print("Hours:", my_calendar.total_working_hours(from_date, to_date, datetime.time(hour=9),
                                                    datetime.time(hour=17, minute=30)))
    print(my_calendar.next_vacation_day())
    print(my_calendar.next_working_day())