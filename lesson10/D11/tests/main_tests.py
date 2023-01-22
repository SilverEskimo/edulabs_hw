from lesson10.D11.CountryCalendar import *

if __name__ == '__main__':
    my_us_calendar = CountryCalendar(
        "US",
        ["Mon", "Tue", "Wed", "Thu", "Fri"],
        2023,
        [
            "01/01/2023",
            "02/01/2023",
            "16/01/2023",
            "20/02/2023",
            "29/05/2023",
            "19/06/2023",
            "04/07/2023",
            "04/09/2023",
            "09/10/2023",
            "10/11/2023",
            "11/11/2023",
            "23/11/2023",
            "25/12/2023",
        ]
    )

    # ######## JANUARY TESTS ######## #
    # Jan - 20 working days, longest span is 3 days from the 14th
    from_day = datetime.datetime(year=2023, month=1, day=1)
    to_day = datetime.datetime(year=2023, month=1, day=31)
    assert my_us_calendar.total_working_days(from_day, to_day) == 20, "Failed in total working days for Jan"
    assert my_us_calendar.longest_holiday_span(from_day, to_day) == (3, datetime.date(2023, 1, 14)), \
        "Failed in longest holiday span for Jan"
    # TODO - please update the day/month according to the day you run it
    assert my_us_calendar.next_working_day() == datetime.date(year=2023, month=1, day=23), \
        "Failed in next working day"
    # TODO - please update the day/month according to the day you run it
    assert my_us_calendar.next_vacation_day() == datetime.date(year=2023, month=1, day=28), \
        "Failed in next vacation day"
    assert my_us_calendar.total_working_hours(from_day, to_day,
                                              datetime.time(hour=9),
                                              datetime.time(hour=17, minute=30)) == 170.0, "Failed in total working" \
                                                                                           "hours Jan"

    # ######## OCTOBER TESTS ######## #
    # Oct - 21 working days, longest span is 3 days from the 7th
    from_day = datetime.datetime(year=2023, month=10, day=1)
    to_day = datetime.datetime(year=2023, month=10, day=31)
    assert my_us_calendar.total_working_days(from_day, to_day) == 21, "Failed in total working days for Oct"
    assert my_us_calendar.longest_holiday_span(from_day, to_day) == (3, datetime.date(2023, 10, 7)), \
        "Failed in longest holiday span for Oct"
    assert my_us_calendar.total_working_hours(from_day, to_day,
                                              datetime.time(hour=8, minute=15),
                                              datetime.time(hour=17, minute=30)) == 194.25, "Failed in total working" \
                                                                                            "hours Oct"



