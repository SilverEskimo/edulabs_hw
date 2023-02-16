from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.frontend.menu.manager_menu import ManagerMenu
from best_bus_ever.src.backend.best_bus_company import BestBusCompany
from best_bus_ever.src.frontend.menu.passenger_menu import PassengerMenu

if __name__ == '__main__':
    best_bus_company = BestBusCompany()

    while True:
        role = Menu.get_user_role()
        if role == 1:
            mm = ManagerMenu()
            count = 0
            password = mm.get_manager_password(count)
            valid = best_bus_company.check_password(password)
            while not valid:
                count += 1
                if count == 3:
                    print("You have entered a wrong password 3 times. Exiting the program.")
                    exit(1)
                password = mm.get_manager_password(count, wrong=True)
                valid = best_bus_company.check_password(password)
            while True:
                action = mm.get_action()
                match action:
                    case 1:
                        print("\nAdd New Route Menu:")
                        line_number = mm.get_line_number()
                        origin = mm.get_origin()
                        destination = mm.get_destination()
                        list_of_stops = mm.get_stops()
                        while True:
                            try:
                                best_bus_company.add_route(line_number, origin, destination, list_of_stops.split(" "))
                                print("\nThe route was successfully added\n")
                            except RouteExistError as e:
                                print(f"\n{e}\n")
                            break
                    case 2:
                        print("\nDelete Route Menu:")
                        line_number = mm.get_line_number()
                        while True:
                            try:
                                best_bus_company.delete_route(line_number)
                            except RouteExistError as e:
                                print(f"\n{e}\n")
                            break
                    case 3:
                        print("\nUpdate Route Menu:")
                        line_number = mm.get_line_number()
                        while True:
                            try:
                                print(f"\n{best_bus_company.get_route(line_number)}\n")
                                actions = mm.get_update_option()
                                if actions[0] == 4:
                                    break
                                for action in actions:
                                    if action == 1:
                                        origin_to_update = mm.get_origin().title()
                                        best_bus_company.update_route(line_number, action, origin_to_update)
                                    elif action == 2:
                                        dest_to_update = mm.get_destination().title()
                                        best_bus_company.update_route(line_number, action, dest_to_update)
                                    elif action == 3:
                                        stops_to_update = mm.get_stops()
                                        best_bus_company.update_route(line_number, action, stops_to_update)
                                print(f"Successfully updated route #{line_number}")
                            except RouteExistError as e:
                                print(f"\n{e}\n")
                            break
                    case 4:
                        print("\nAdd Scheduled Ride Menu:")
                        line_number = Menu.get_line_number()
                        while True:
                            try:
                                scheduled_rides = best_bus_company.get_scheduled_rides_for_route(line_number)
                                if not scheduled_rides:
                                    print("\nThere are no scheduled rides as of now\n")
                                else:
                                    print("Current scheduled rides: ")
                                    for ride in scheduled_rides:
                                        print(f"Ride ID: {ride[0]}\nRide Details:\n{ride[1]}\n")
                                while True:
                                    try:
                                        ride_details = mm.get_scheduled_ride()
                                        best_bus_company.add_scheduled_ride(line_number, ride_details)
                                        print("\nSuccessfully added a new scheduled ride!\n")
                                    except WrongTimeFormat as e:
                                        print(f"\n{e}\n")
                                    break
                            except RouteExistError as e:
                                print(f"\n{e}\n")
                            break
                    case 5:
                        break
        elif role == 2:
            pm = PassengerMenu()
            while True:
                action = pm.get_action()
                match action:
                    case 1 | 2:
                        if action == 1:
                            print("\nSearch Route Menu:")
                        if action == 2:
                            print("\nReport Delay Menu:")
                        search_term = pm.get_search_route_menu()
                        match search_term:
                            case 1:
                                print("Searching by line number")
                                line_number = pm.get_line_number()
                                try:
                                    route = best_bus_company.search_route(search_term, line_number)
                                    print(f"\n{route}\n")
                                    if action == 2:
                                        pass
                                except RouteExistError as e:
                                    print(f"\n{e}\n")
                            case 2:
                                print("Searching by origin")
                                origin = pm.get_origin()
                                try:
                                    route = best_bus_company.search_route(search_term, origin.lower())
                                    for r in route:
                                        print(f"\n{r}Stops:", end=" ")
                                        for s in r.stops:
                                            print(s, end=" ")
                                        for sr in r.scheduled_rides:
                                            print(f"\nRide ID: {sr[0]}\n{sr[1]}")
                                except RouteExistError as e:
                                    print(f"\n{e}\n")
                            case 3:
                                print("Searching by destination")
                                destination = pm.get_destination()
                                try:
                                    route = best_bus_company.search_route(search_term, destination.lower())
                                    for r in route:
                                        print(f"\n{r}Stops:", end=" ")
                                        for s in r.stops:
                                            print(s, end=" ")
                                        for sr in r.scheduled_rides:
                                            print(f"\nRide ID: {sr[0]}\n{sr[1]}")
                                except RouteExistError as e:
                                    print(f"\n{e}\n")
                            case 4:
                                print("Searching by bus stop")
                                bus_stop = pm.get_stop()
                                try:
                                    route = best_bus_company.search_route(search_term, bus_stop.lower())
                                    for r in route:
                                        print(f"\n{r}Stops:", end=" ")
                                        for s in r.stops:
                                            print(s, end=" ")
                                        for sr in r.scheduled_rides:
                                            print(f"\n\nRide ID: {sr[0]}\n{sr[1]}")
                                except RouteExistError as e:
                                    print(f"\n{e}\n")
                    case 2:
                        pass
                    case 3:
                        break
        elif role == 3:
            print("Thank you. Bye Bye!")
            exit(0)










