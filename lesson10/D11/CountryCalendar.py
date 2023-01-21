import datetime

WEEK_DAYS = {0, 1, 2, 3, 4, 5, 6}


class CountryCalendar:
    def __init__(self, name: str, work_days: list, year: int, public_holidays: list):
        """
        Country Calendar class initiation
        :param name:
        :param work_days:
        :param year:
        :param public_holidays:
        """
        self.__name = name
        self.__work_days = work_days
        self.__year = year
        self.__public_holidays = public_holidays
        self.__weekend_days = WEEK_DAYS - set(work_days)

    def total_working_days(self, from_date: datetime.date, to_date: datetime.date, next_working=False) -> \
            int | datetime.datetime:
        """
        given 2 datetime.date objects, return the amount of working days in this range
        :param next_working:
        :param from_date:
        :param to_date:
        :return:
        Number of working days - int
        """
        working_days = 0
        start_date = from_date
        while start_date <= to_date:
            if start_date.weekday() not in self.__weekend_days \
                    and start_date not in self.__public_holidays:
                working_days += 1
                if next_working and working_days == 1:
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
        """
        vacation_days = 0
        start_date = from_date
        while start_date <= to_date:
            if start_date.weekday() in self.__weekend_days \
                    or start_date in self.__public_holidays:
                vacation_days += 1
            if next_vacation and vacation_days == 1:
                return start_date
            start_date += datetime.timedelta(1)
        return vacation_days

    def total_working_hours(self, from_datetime, to_datetime, start_working_time, end_working_time) -> float:
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

        minutes_to_add = (float(end_min) - float(start_min)) / 60
        working_hours += minutes_to_add

        return working_hours * self.total_working_days(from_datetime, to_datetime)

    def next_vacation_day(self) -> str:
        """
        return datetime.date object of the upcoming vacation day starting from now
        :return:
        """
        today = datetime.datetime.now()
        while today.weekday() in self.__weekend_days or today in self.__public_holidays:
            today += datetime.timedelta(1)
        end_date = today + datetime.timedelta(7)
        return (self.total_vacation_days(today, end_date, next_vacation=True)).strftime("%B %d, %Y")

    def next_working_day(self):
        """
        return datetime.date object of the upcoming working day starting from now
        :return:
        """
        today = datetime.datetime.now()
        while today.weekday() in self.__weekend_days or today in self.__public_holidays:
            today += datetime.timedelta(1)
        end_date = today + datetime.timedelta(7)
        return (self.total_working_days(today, end_date, next_working=True)).strftime("%B %d, %Y")

    def longest_holiday_span(self, from_date, to_date):
        """
        given 2 datetime.date objects, return the amount of days and the beginning date of the longest vacation
        span between the given two dates.
        :param from_date:
        :param to_date:
        :return:
        """
        pass
