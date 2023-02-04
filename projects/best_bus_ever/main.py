from best_bus_ever.src.exceptions import *
from best_bus_ever.src.backend.utils import Utils
from best_bus_ever.src.frontend.utils.user_input import UserInput
from best_bus_ever.src.backend.best_bus_company import BestBusCompany


if __name__ == '__main__':
    user_input = UserInput()
    best_bus_company = BestBusCompany()
    role = user_input.get_user_role()
    utils = Utils()

    if role == 1:
        count = 0
        password = user_input.get_manager_password()
        valid = best_bus_company.check_password(password)
        while not valid:
            count += 1
            if count == 3:
                print("You have entered a wrong password 3 times. Exiting the program.")
                exit(1)
            password = user_input.get_manager_password(wrong=True)
            valid = best_bus_company.check_password(password)
        action = user_input.get_manager_action()
        match action:
            case 1:
                line_number = user_input.get_line_number()
                origin = user_input.get_origin()
                destination = user_input.get_destination()
                rides = user_input.get_scheduled_rides()
                list_of_stops = user_input.get_stops()
                converted_rides = utils.convert_rides(rides)
                while True:
                    try:
                        best_bus_company.add_route(line_number, origin, destination, list_of_stops, converted_rides)
                        break
                    except RouteExistError as e:
                        print(e)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
    else:
        action = user_input.get_passenger_action()










