import datetime
import random

from best_bus_ever.src.utils.utils import Utils
from best_bus_ever.src.backend.scheduled_ride import ScheduledRide


class BusRoute:
    def __init__(self,
                 line_number: int,
                 origin: str,
                 destination: str,
                 list_of_stops: list):
        self._line_number = line_number
        self._origin = origin.title()
        self._destination = destination.title()
        self._list_of_stops = list_of_stops
        self._scheduled_rides: dict[int, ScheduledRide] = {}

    @property
    def scheduled_rides(self):
        return self._scheduled_rides.items()

    @scheduled_rides.setter
    def scheduled_rides(self, ride_details: tuple):
        converted_times = Utils.convert_ride_times(ride_details[:2])
        ride_id = random.randint(1, 100000)
        new_ride = ScheduledRide(ride_id, converted_times[0], converted_times[1], ride_details[2])
        self._scheduled_rides[ride_id] = new_ride

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @property
    def stops(self):
        return self._list_of_stops

    @stops.setter
    def stops(self, stops: str):
        self._list_of_stops = stops.split(",")

    def __str__(self):
        return f"Line number: {self._line_number}\n" \
               f"Origin: {self._origin}\n" \
               f"Destination: {self._destination}\n"



