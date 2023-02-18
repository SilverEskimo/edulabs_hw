from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class PassengerMenu(Menu):
    def __init__(self):
        super().__init__()

    def get_action(self):
        msg = "\nPlease choose 1 of the following actions:\n" \
              "(1) Search Route\n" \
              "(2) Report Delay\n" \
              "(3) Exit\n" \
              "Your choice (1, 2 or 3): "
        while True:
            try:
                action = input(msg).strip()
                UserInputValidation.valid_passenger_action(action)
                break
            except WrongPassengerAction as e:
                print(f"\n{e}\n")
        return int(action)

    @staticmethod
    def get_search_route_menu():
        msg = "\nPlease choose one of the following searching options:\n(1) By Line Number\n(2) By Origin\n" \
              "(3) By Destination\n(4) By Bus Stop\n(5) Back to main menu\nYour choice: "
        while True:
            try:
                search_term = input(msg).strip()
                valid_search_term = UserInputValidation.valid_search_term(search_term)
                break
            except WrongSearchTerm as e:
                print(f"\n{e}\n")
        return valid_search_term

