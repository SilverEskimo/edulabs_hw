import datetime
from lesson10.D11.CountryCalendar import *

if __name__ == '__main__':
    my_calendar = CountryCalendar(
        "Israel",
        ["Sun", "Mon", "Tue", "Wed", "Thu"],
        2023,
        [
            "20/09/2022",
            "21/09/2022",
            "22/09/2022",
            "09/10/2022",
            "10/10/2022",
            "11/10/2022",
            "12/10/2022",
            "13/10/2022"

        ]
    )
    from_date = datetime.datetime(year=2022, month=9, day=19)
    to_date = datetime.datetime(year=2022, month=10, day=31)
    print("Working days:", my_calendar.total_working_days(from_date, to_date))
    print("Vacation Days:", my_calendar.total_vacation_days(from_date, to_date))
    print("Hours:", my_calendar.total_working_hours(from_date, to_date, datetime.time(hour=9),
                                                    datetime.time(hour=17, minute=30)))
    print("Next vacation:", my_calendar.next_vacation_day())
    print("Next work day:", my_calendar.next_working_day())
    print("Longest Span:", my_calendar.longest_holiday_span(from_date.date(), to_date.date()))
