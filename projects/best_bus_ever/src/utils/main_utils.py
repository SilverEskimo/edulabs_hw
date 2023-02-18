from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.frontend.menu.manager_menu import ManagerMenu
from best_bus_ever.src.backend.best_bus_company import BestBusCompany
from best_bus_ever.src.frontend.menu.passenger_menu import PassengerMenu


class MainUtils:
    def __init__(self, bus_company: BestBusCompany):
        self._best_bus_company = bus_company
        self._mm = ManagerMenu()
        self._pm = PassengerMenu()

    @staticmethod
    def _print_single_route(route):
        print(f"\n{25 * '*'}")
        print(f"{route}Stops:", end=" ")
        for s in route.stops:
            print(s, end=" ")
        if route.scheduled_rides:
            print("\n\nScheduled Rides:")
        else:
            print("\n\nThere are no scheduled rides for this line")
        for sr in route.scheduled_rides:
            print(25 * "-")
            print(f"Ride ID: {sr[0]}\n{sr[1]}Delays:")
            if not sr[1].delays:
                print("There are no reported delays for this ride")
            else:
                for delay_date, delay in sr[1].delays:
                    print(f"{delay_date.strftime('%d/%m/%Y')} - {delay} minutes")

    @staticmethod
    def _print_routes(routes):
        for r in routes:
            MainUtils._print_single_route(r)

    def password(self):
        count = 0
        password = self._mm.get_manager_password(count)
        valid = self._best_bus_company.check_password(password)
        while not valid:
            count += 1
            if count == 3:
                print("You have entered a wrong password 3 times. Exiting the program.")
                exit(1)
            password = self._mm.get_manager_password(count, wrong=True)
            valid = self._best_bus_company.check_password(password)

    def _search_route(self, search_term):
        match search_term:
            case 1:
                print("Searching by line number")
                line_number = self._pm.get_line_number()
                try:
                    route = self._best_bus_company.search_route(search_term, line_number)
                    self._print_single_route(route)
                    return route
                except RouteExistError as e:
                    print(f"\n{e}\n")
            case 2:
                print("Searching by origin")
                origin = self._pm.get_origin()
                try:
                    route = self._best_bus_company.search_route(search_term, origin.lower())
                    self._print_routes(route)
                    return route
                except RouteExistError as e:
                    print(f"\n{e}\n")
            case 3:
                print("Searching by destination")
                destination = self._pm.get_destination()
                try:
                    route = self._best_bus_company.search_route(search_term, destination.lower())
                    self._print_routes(route)
                    return route
                except RouteExistError as e:
                    print(f"\n{e}\n")
            case 4:
                print("Searching by bus stop")
                bus_stop = self._pm.get_stop()
                try:
                    route = self._best_bus_company.search_route(search_term, bus_stop.lower())
                    self._print_routes(route)
                    return route
                except RouteExistError as e:
                    print(f"\n{e}\n")
            case 5:
                print("Going Back to passenger menu")
                return

    def _add_route_action(self):
        print("\nAdd New Route Menu:")
        line_number = self._mm.get_line_number()
        origin = self._mm.get_origin()
        destination = self._mm.get_destination()
        list_of_stops = self._mm.get_stops()
        while True:
            try:
                self._best_bus_company.add_route(line_number, origin, destination, list_of_stops.split(" "))
                print(f"\nSuccessfully added new route #{line_number}\n")
            except RouteExistError as e:
                print(f"\n{e}\n")
            break

    def _delete_route_action(self):
        print("\nDelete Route Menu:")
        line_number = self._mm.get_line_number()
        while True:
            try:
                self._best_bus_company.delete_route(line_number)
                print(f"\nSuccessfully deleted route #{line_number}\n")
            except RouteExistError as e:
                print(f"\n{e}\n")
            break

    def _update_route_action(self):
        print("\nUpdate Route Menu:")
        line_number = self._mm.get_line_number()
        while True:
            try:
                print(f"\n{self._best_bus_company.get_route(line_number)}\n")
                actions = self._mm.get_update_option()
                if actions[0] == 4:
                    break
                for action in actions:
                    if action == 1:
                        origin_to_update = self._mm.get_origin().title()
                        self._best_bus_company.update_route(line_number, action, origin_to_update)
                    elif action == 2:
                        dest_to_update = self._mm.get_destination().title()
                        self._best_bus_company.update_route(line_number, action, dest_to_update)
                    elif action == 3:
                        stops_to_update = self._mm.get_stops()
                        self._best_bus_company.update_route(line_number, action, stops_to_update)
                print(f"\nSuccessfully updated route #{line_number}\n")
            except RouteExistError as e:
                print(f"\n{e}\n")
            break

    def _add_scheduled_ride_action(self):
        print("\nAdd Scheduled Ride Menu:")
        line_number = Menu.get_line_number()
        while True:
            try:
                scheduled_rides = self._best_bus_company.get_scheduled_rides_for_route(line_number)
                if not scheduled_rides:
                    print("\nThere are no scheduled rides as of now")
                else:
                    print("\nCurrent scheduled rides: ")
                    for ride in scheduled_rides:
                        print(25 * "-")
                        print(f"Ride ID: {ride[0]}\nRide Details:\n{ride[1]}Driver: {ride[1].driver}")
                        print(f"")
                while True:
                    try:
                        ride_details = self._mm.get_scheduled_ride()
                        self._best_bus_company.add_scheduled_ride(line_number, ride_details)
                        print("\nSuccessfully added a new scheduled ride!\n")
                    except WrongTimeFormat as e:
                        print(f"\n{e}\n")
                    break
            except RouteExistError as e:
                print(f"\n{e}\n")
            break

    def _search_route_action(self):
        print("\nSearch Route Menu:")
        search_term = self._pm.get_search_route_menu()
        self._search_route(search_term)

    def _report_delay_action(self):
        print("\nReport Delay Menu:")
        search_term = self._pm.get_search_route_menu()
        if self._search_route(search_term):
            ride_input = Menu.get_scheduled_ride_id()
            try:
                ride_to_update = self._best_bus_company.search_route(5, ride_input)
                delay = Menu.get_delay_in_mins()
                date = Menu.get_delay_date()
                ride_to_update.add_delay(date.date(), delay)
                print("\nDelay was added successfully!\n")
            except WrongRideId as e:
                print(f"\n{e}\n")
            except WrongDelayFormat as e:
                print(f"\n{e}\n")
            except WrongDateFomat as e:
                print(f"\n{e}\n")

    def manager_action(self):
        while True:
            action = self._mm.get_action()
            match action:
                case 1:
                    self._add_route_action()
                    self._best_bus_company.save_data()
                case 2:
                    self._delete_route_action()
                    self._best_bus_company.save_data()
                case 3:
                    self._update_route_action()
                    self._best_bus_company.save_data()
                case 4:
                    self._add_scheduled_ride_action()
                    self._best_bus_company.save_data()
                case 5:
                    break

    def passenger_action(self):
        while True:
            action = self._pm.get_action()
            match action:
                case 1:
                    self._search_route_action()
                    self._best_bus_company.save_data()
                case 2:
                    self._report_delay_action()
                    self._best_bus_company.save_data()
                case 3:
                    break
