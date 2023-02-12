from best_bus_ever.src.backend.bus_route import BusRoute
from best_bus_ever.src.utils.exceptions import *


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
                  stops: list):
        new_route = BusRoute(line_number, origin, destination, stops)
        if self._routes.get(line_number):
            raise RouteExistError("Error: this route already exists")
        self._routes[line_number] = new_route
        return new_route

    def delete_route(self, route_id: int):
        if not self._routes.get(route_id):
            raise RouteExistError("Error: trying to delete a non existing route")
        self._routes.pop(route_id)

    def update_route(self, route_id: int, action: int, value: str | list[str]):
        try:
            route_to_update = self.get_route(route_id)
            if action == 1:
                route_to_update.set_origin(value)
            elif action == 2:
                route_to_update.set_destination(value)
            elif action == 3:
                route_to_update.set_stops(value)
        except RouteExistError as e:
            print(f"\n{e}\n")

    def get_route(self, route_id):
        if not self._routes.get(route_id):
            raise RouteExistError("Error: this route does not exist")
        route: BusRoute = self._routes.get(route_id)
        return route

    def get_scheduled_rides_for_route(self, route_id):
        if not self.get_route(route_id):
            raise RouteExistError("Error: this route does not exist")
        return self.get_route(route_id).get_scheduled_rides()

    def add_scheduled_ride(self, route_id, ride_details: tuple):
        route_to_update = self.get_route(route_id)
        if not route_to_update:
            raise RouteExistError("Error: this route does not exist")
        route_to_update.set_scheduled_rides(ride_details)

    def search_route(self, search_term: int, value: str | int):
        if search_term == 1:
            try:
                return self.get_route(value)
            except RouteExistError:
                raise RouteExistError("Error: this route does not exits")
        if search_term == 2:
            pass
        if search_term == 3:
            pass
        if search_term == 4:
            pass
        return

    def get_routes(self) -> dict[int, BusRoute]:
        return self._routes
