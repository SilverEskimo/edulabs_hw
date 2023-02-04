import datetime


class ScheduledRide:
    def __init__(self, date: datetime.datetime):
        self._date = date

    def get_date(self):
        return self._date
    def __str__(self):
        return self._date
