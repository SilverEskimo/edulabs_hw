from best_bus_ever.src.backend.bus_route import BusRoute
from best_bus_ever.src.backend.scheduled_ride import ScheduledRide
from best_bus_ever.src.exceptions import *


class BestBusCompany:
    def __init__(self):
        self._manager_password = "RideWithUs!"
        self._routes = {}

    def check_password(self, password: str):
        return self._manager_password == password

    def add_route(self,
                  line_number: int,
                  origin: str,
                  destination: str,
                  stops: list,
                  scheduled_rides: list[ScheduledRide]):
        new_route = BusRoute(line_number, origin, destination, stops, scheduled_rides)
        if self._routes.get(line_number):
            raise RouteExistError("Error: this route already exists")
            return
        self._routes[line_number] = new_route
        return new_route

    def get_routes(self) -> dict[int, BusRoute]:
        return self._routes
