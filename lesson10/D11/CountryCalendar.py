import datetime

MINS_IN_HOUR = 60
WEEK_DAYS_SET = {0, 1, 2, 3, 4, 5, 6}
WEEK_DAYS_DICT = {
    "sun": 6,
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sunday": 6,
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
}


class CountryCalendar:
    def __init__(self, name: str, work_days: list, year: int, public_holidays: list):
        """
        Country Calendar class initiation
        :param name: str - name of the calendar (for example: 'Israel')
        :param work_days: list - working days (for example: ["Mon", "Tue", "Wed"...])
        :param year: int - calendar's year (for example: 2023)
        :param public_holidays: list - public holidays dates (for example: ["25/12/2023", "01/01/2023"...])
        """
        self.__name = name
        self.__work_days = [WEEK_DAYS_DICT[day.lower()] for day in work_days]
        self.__year = year
        self.__public_holidays = [datetime.datetime.strptime(holiday, "%d/%m/%Y").date() for holiday in public_holidays]
        self.__weekend_days = WEEK_DAYS_SET - set(self.__work_days)

    def total_working_days(self, from_date: datetime.date, to_date: datetime.date, next_working=False) -> \
            int | datetime.datetime:
        """
        given 2 datetime.date objects, return the amount of working days in this range
        :param next_working:
        :param from_date:
        :param to_date:
        :return:
        Number of working days - int | next working day if next_param=True - datetime.datetime
        """
        working_days = 0
        start_date = from_date
        while start_date <= to_date:
            if start_date.weekday() not in self.__weekend_days \
                    and start_date.date() not in self.__public_holidays:
                working_days += 1
                if next_working and start_date != from_date:
                    return start_date
            start_date += datetime.timedelta(1)
        return working_days

    def total_vacation_days(self, from_date: datetime.datetime, to_date: datetime.datetime, next_vacation=False) -> \
            int | datetime.datetime:
        """
        given 2 datetime.date objects, return the amount of vacation in this range (vacation days are either public
        holidays or weekends)
        :param next_vacation:
        :param from_date:
        :param to_date:
        :return:
        Number of vacations days - int | next vacation day if next_vacation=True - datetime.datetime
        """
        vacation_days = 0
        start_date = from_date
        while start_date <= to_date:
            if start_date.weekday() in self.__weekend_days \
                    or start_date.date() in self.__public_holidays:
                vacation_days += 1
                if next_vacation and start_date != from_date:
                    return start_date
            start_date += datetime.timedelta(1)
        return vacation_days

    def total_working_hours(self,
                            from_datetime: datetime.datetime,
                            to_datetime: datetime.datetime,
                            start_working_time: datetime.time,
                            end_working_time: datetime.time
                            ) -> float:
        """
        given 2 datetime.datetime objects and 2 datetime.time objects, return total amount of working hours
        (float) between these two days
        :param from_datetime:
        :param to_datetime:
        :param start_working_time:
        :param end_working_time:
        :return:
        Total working hours between 2 dates - float
        """
        start_hour, start_min, _ = str(start_working_time).split(":")
        end_hour, end_min, _ = str(end_working_time).split(":")
        working_hours = int(end_hour) - int(start_hour)

        minutes_to_add = (float(end_min) - float(start_min)) / MINS_IN_HOUR
        working_hours += minutes_to_add

        return working_hours * self.total_working_days(from_datetime, to_datetime)

    def next_vacation_day(self) -> datetime.date:
        """
        :return:
        return datetime.date object of the upcoming vacation day starting from now - datetime.date
        """
        today = datetime.datetime.now()
        end_date = today + datetime.timedelta(7)
        return self.total_vacation_days(today, end_date, next_vacation=True).date()

    def next_working_day(self) -> datetime.date:
        """
        :return:
        return datetime.date object of the upcoming working day starting from now - datetime.date
        """
        today = datetime.datetime.now()
        end_date = today + datetime.timedelta(364)
        return self.total_working_days(today, end_date, next_working=True).date()

    def longest_holiday_span(self, from_date: datetime.date, to_date: datetime.date) -> (int, datetime.date):
        """
        given 2 datetime.date objects, return the amount of days and the beginning date of the longest vacation
        span between the given two dates.
        :param from_date:
        :param to_date:
        :return:
        return the amount of days and the beginning date of the longest vacation - (int,datetime.date)
        """
        start_date = from_date.date()
        previous_date = (from_date - datetime.timedelta(1)).date()
        longest_span = 0
        span_count = 0
        first_date = from_date
        while start_date <= to_date.date():
            if start_date.weekday() in self.__weekend_days or start_date in self.__public_holidays:
                if previous_date + datetime.timedelta(1) == start_date:
                    span_count += 1
                if span_count > longest_span:
                    longest_span = span_count
                    first_date = start_date - datetime.timedelta(longest_span - 1)
            else:
                span_count = 0
            previous_date = start_date
            start_date += datetime.timedelta(1)
        return longest_span, first_date

    def __str__(self):
        return f"Calendar Name: {self.__name}\nYear: {self.__year}\nPublic Holidays: {self.__public_holidays}"
