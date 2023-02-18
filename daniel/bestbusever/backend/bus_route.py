import random
from bestbusever.backend.scheduled_ride import ScheduledRide

class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, list_of_stops: list[str]):
        self._line_number = line_number
        self._origin = origin
        self._destination = destination
        self._list_of_stops = list_of_stops
        self._scheduled_rides = {}

    def add_scheduled_ride(self, origin_time, destination_time, driver):
        ride_id = random.randint(1, 1000)
        if self._scheduled_rides.get(ride_id):
            raise Exception("Ride ID already exist!")
        scheduled_ride = ScheduledRide(origin_time, destination_time, driver)
        self._scheduled_rides[ride_id] = scheduled_ride
        return self

    def set_origin(self, new_origin):
        self._origin = new_origin

    def set_destination(self, new_destination):
        self._destination = new_destination

    def set_stops(self, stops):
        self._list_of_stops = stops

    def __repr__(self):
        return f"Line number: {self._line_number}\n"\
               f"Origin: {self._origin}\n" \
               f"Destination: {self._destination}\n" \
               f"List of stops: {self._list_of_stops}\n" \
               f"Rides: {self._scheduled_rides}"




