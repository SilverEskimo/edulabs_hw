import datetime
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
        self._scheduled_rides: list[ScheduledRide] = []

    def set_scheduled_rides(self, ride_details: tuple):
        converted_times = Utils.convert_ride_times(ride_details[:2])
        new_ride = ScheduledRide(self._line_number, converted_times[0], converted_times[1], ride_details[2])
        self._scheduled_rides.append(new_ride)

    def get_scheduled_rides(self):
        return self._scheduled_rides

    def set_origin(self, origin):
        self._origin = origin

    def set_destination(self, destination):
        self._destination = destination

    def set_stops(self, stops):
        self._list_of_stops = stops

    def __repr__(self):
        return f"Line number: {self._line_number}\nOrigin: {self._origin}\nDestination: {self._destination}\n" \
               f"Stops: {self._list_of_stops}\nRides: {self.get_scheduled_rides()}"


if __name__ == '__main__':
    sr = ScheduledRide(1, datetime.time(hour=10, minute=20), datetime.time(hour=10, minute=51), "Yossi")
    sr1 = ScheduledRide(2, datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=51), "Asher")
    b = BusRoute(1, "ala", "blaa", ["asd", "Adwe", "asd"], [sr, sr1])
    print(b)


