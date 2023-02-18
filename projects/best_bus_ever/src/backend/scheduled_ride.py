import datetime


class ScheduledRide:
    def __init__(self,
                 ride_id: int,
                 origin_time: datetime.time,
                 dest_time: datetime.time,
                 driver_name: str):
        self._ride_id = ride_id
        self._origin_time = origin_time
        self._dest_time = dest_time
        self._driver_name = driver_name
        self._delays = {}

    def get_time(self):
        return self._origin_time, self._dest_time

    @property
    def driver(self):
        return self._driver_name

    @driver.setter
    def driver(self, driver_name: str):
        self._driver_name = driver_name

    @property
    def delays(self):
        return self._delays.items()

    def add_delay(self, delay_date: datetime.date, delay_time: float):
        self._delays[delay_date] = delay_time

    @property
    def ride_id(self):
        return self._ride_id

    def __str__(self):
        return f"Origin time: {self._origin_time.strftime('%H:%M')}\n" \
               f"Destination time: {self._dest_time.strftime('%H:%M')}\n"


