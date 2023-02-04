from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.exceptions import *
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class PassengerMenu(Menu):
    def __init__(self):
        super().__init__()
        self._user_input_validation = UserInputValidation()

    def get_action(self):
        msg = "Please choose 1 of the following actions:\n(1) Search Route\n(2) Report Delay\nYour choice (1 or 2): "
        while True:
            try:
                action = input(msg).strip()
                self._user_input_validation.valid_passenger_action(action)
                break
            except WrongPassengerAction as e:
                print(f"\n{e}\n")
        return action


if __name__ == '__main__':
    m = PassengerMenu()
    m.get_action()
