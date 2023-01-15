# Write a function that helps organize manually inserted catalog of  Volvo cars and returns the changed catalog:
# Function receives an existing catalog, asks the user to insert details about the new vehicle (single vehicle),
# and returns the updated catalog. Your mission is to define the structure of the catalog.
# The details entered for each vehicle are as follows:
from pprint import pprint

const_type = ("private", "semi-truck")
const_models = ("s-30", "s-40", "s-600", "s-80", "s-90", "vnl-760", "vnl-860",
                "vnl-300", "vnl-600", "vnl-500", "vnl-900")
const_motor = ("diesel", "petrol", "electric", "hydrogen")
const_colors = ("orange", "green", "violet", "red-orange", "yellow-orange", "yellow-green", "blue-green",
                "blue-violet, red-violet")

vehicles = {
    "private": {
        2001: {
            "s-30": {
                0: {
                    "motor": "diesel",
                    "color": "green"
                }
            },
            "s-40": {

            }
        }
    },
    "semi-truck": {
        "vnl-300": {
            0: {
                "motor": "diesel",
                "color": "violet"
            }
        }
    }
}


def current_catalog():
    catalog_type = input("Which catalog do you wish to see? ('private', 'semi-truck', 'both'): ").strip()
    if catalog_type == "both":
        return vehicles
    return vehicles.get(catalog_type)


def enter_new_vehicle():
    while True:
        vehicle_type = input("Which type of vehicle are you adding? ('private', 'semi-truck'): ").strip().lower()
        if vehicle_type not in const_type:
            vehicle_type = input(f"Wrong type, please enter 'private' or 'semi-truck': ").strip().lower()
        else:
            year = input("Please enter the year of production in the following format yyyy: ").strip()
            if not year.isdigit() or len(year) != 4:
                year = input("Wrong year input, please try again")
            else:
                while True:
                    model = input(f"Please enter the model from the possible options:\n{const_models}\n"
                                  f"Your input: ").strip().lower()
                    if model not in const_models:
                        model = input(f"This model doesn't exist. Please choose from:\n{const_models}\n"
                                      f"Your input: ").strip().lower()
                    else:
                        motor = input(f"Please enter the type of the motor from the available options:\n{const_motor}\n"
                                      f"Your input: ").strip().lower()
                        if motor not in const_motor:
                            motor = input(f"This motor doesn't exist. Please choose from:\n{const_models}\n"
                                          f"Your input: ").strip().lower()
                        else:
                            color = input(f"Please enter the color from the possible options:\n{const_colors}\n"
                                          f"Your input: ").strip().lower()
                            if color not in const_colors:
                                color = input(f"This color doesn't exist. Please choose from:\n{const_colors}\n"
                                              f"Your input: ").strip().lower()
                            else:
                                if vehicles.get(vehicle_type).get(int(year), {}):
                                    if vehicles.get(vehicle_type).get(int(year)).get(model):
                                        num_of_vehicles = len(vehicles.get(vehicle_type).get(int(year)).get(model))
                                        vehicles[vehicle_type][int(year)][model][num_of_vehicles] = {"motor": motor, "color": color}
                                        break
                                else:
                                    vehicles[vehicle_type][int(year)] = {}
                                    vehicles[vehicle_type][int(year)][model] = {}
                                    vehicles[vehicle_type][int(year)][model][0] = {"motor": motor, "color": color}
                                    break
                                pprint(vehicles)


def get_user_choice():
    while True:
        choice = input("Welcome to Volvo catalog! Please enter your choice:\n1 to show current catalog"
                       "\n2 to enter new vehicle\nYour choice: ").strip()
        match choice:
            case "1":
                pprint(current_catalog())
                proceed = input("Do you want to proceed to entering the details? (y for yes, quit for no): ").strip()
                if proceed.lower() == "quit":
                    print("See you later!")
                    break
                else:
                    enter_new_vehicle()
                    break
            case "2":
                enter_new_vehicle()
                break
            case other:
                choice = input("Wrong input, please try again (1 or 2): ")

# def volvo_catalog(current_catalog):
#     user_input = get_input()
#     return updated_catalog


get_user_choice()