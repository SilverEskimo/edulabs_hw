from best_bus_ever.src.backend.scheduled_ride import ScheduledRide


class BusRoute:
    def __init__(self,
                 line_number: int,
                 origin: str,
                 destination: str,
                 list_of_stops: list,
                 scheduled_rides: list[ScheduledRide]):
        self._line_number = line_number
        self._origin = origin
        self._destination = destination
        self._list_of_stops = list_of_stops
        self._scheduled_rides = scheduled_rides

    def get_route(self):
        return self._scheduled_rides
    def __str__(self):
        return f"Line number: {self._line_number}\nScheduled Rides:\n{self._scheduled_rides}"



