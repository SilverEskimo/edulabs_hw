import pickle
from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.backend.bus_route import BusRoute


class BestBusCompany:
    def __init__(self):
        self._manager_password = "RideWithUs!"
        self._routes = {}
    error_message = "Error: this route does not exist"

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
                route_to_update.origin = value
            elif action == 2:
                route_to_update.destination = value
            elif action == 3:
                route_to_update.stops = value
        except RouteExistError as e:
            print(f"\n{e}\n")

    def get_route(self, route_id):
        if not self._routes.get(route_id):
            raise RouteExistError(BestBusCompany.error_message)
        route: BusRoute = self._routes.get(route_id)
        return route

    def get_scheduled_rides_for_route(self, route_id):
        if not self.get_route(route_id):
            raise RouteExistError(BestBusCompany.error_message)
        return self.get_route(route_id).scheduled_rides

    def add_scheduled_ride(self, route_id, ride_details: tuple):
        route_to_update = self.get_route(route_id)
        if not route_to_update:
            raise RouteExistError(BestBusCompany.error_message)
        route_to_update.scheduled_rides = ride_details

    def search_route(self, search_term: int, value_to_search: str | int):
        if search_term == 1:
            try:
                return self.get_route(value_to_search)
            except RouteExistError:
                raise RouteExistError(BestBusCompany.error_message)
        if search_term == 2 or search_term == 3:
            ret_list = []
            if search_term == 2:
                for key, value in self._routes.items():
                    if value.origin.lower() == value_to_search:
                        ret_list.append(value)
            else:
                for key, value in self._routes.items():
                    if value.destination.lower() == value_to_search:
                        ret_list.append(value)
            if not ret_list:
                raise RouteExistError("Error: this origin/destination does not belong to any route")
            return ret_list
        if search_term == 4:
            ret_list = []
            for key, value in self._routes.items():
                for stop in value.stops:
                    if stop.lower() == value_to_search:
                        ret_list.append(value)
            if not ret_list:
                raise RouteExistError("Error: there is not route with the provided stop")
            return ret_list
        if search_term == 5:
            for i, route in self._routes.items():
                for j, ride in route.scheduled_rides:
                    if value_to_search == ride.ride_id:
                        return ride
            raise WrongRideId("Error: the provided ride ID does not exist")

    def get_routes(self) -> dict[int, BusRoute]:
        return self._routes

    def save_data(self):
        with open('bus_company.pickle', 'wb') as fh:
            pickle.dump(self, fh)
