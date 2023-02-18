from daniel.bestbusever.frontend.menu import Menu
from daniel.bestbusever.backend.bestbus import BestBusCompany

if __name__ == '__main__':
    role = Menu.main_menu()
    best_bus = BestBusCompany()
    while True:
        if role == 1:
            action = Menu.passenger_menu()
            match action:
                case 1:
                    srch = Menu.search_by()
                    line = Menu.get_line_number()
                    searched_route = best_bus.search_by_line(line)
                    print(searched_route)
                    print("Searching Route")
                case 2:
                    print("Reporting Delay")
                case 3:
                    print("Exiting")

        elif role == 2:
            action = Menu.manager_menu()
            match action:
                case 1:
                    print("Adding a new route")
                    line_number = Menu.get_line_number()
                    origin = Menu.get_origin()
                    destination = Menu.get_destination()
                    list_of_stops = Menu.get_list_stop()
                    try:
                        new_route = best_bus.start_route(line_number, origin, destination, list_of_stops)
                    except Exception as e:
                        print(e)
                    print(best_bus)
                    continue
                case 2:
                    print("Deleting Route by Line number: ")
                    delete = Menu.delete_route()
                    ask = input("Are you sure? y/n ")
                    if "y" in ask:
                        new_route = best_bus.delete_ride(delete)
                        print(best_bus)
                    if "n" in ask:
                        continue
                case 3:
                    print("Updating Route")
                    line_number = Menu.get_line_number()
                    try:
                        update_val = Menu.update_route()
                        if "1" in update_val:
                            new_origin = Menu.get_origin()
                            best_bus.update_route_info(line_number, origin=new_origin)
                        if "2" in update_val:
                            new_destination = Menu.get_destination()
                            best_bus.update_route_info(line_number, destination=new_destination)
                        if "3" in update_val:
                            new_list_of_stops = Menu.get_list_stop()
                            best_bus.update_route_info(line_number, list_of_stops=new_list_of_stops)
                        print(best_bus.get_route_by_line(line_number))
                    except Exception as e:
                        print(e)
                case 4:
                        line_number = Menu.get_line_number()
                        if line_number in new_route.keys():
                            print(new_route.get(line_number))
                        driver = Menu.get_driver()
                        origin_time = Menu.get_origin_time()
                        dest = Menu.get_dest_time()
                        print(best_bus.add_sched_to_route(line_number, origin_time, dest, driver))

                case 5:
                    print("Exiting")
                    break



