from best_bus_ever.src.exceptions import *
from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class ManagerMenu(Menu):
    def __init__(self):
        super().__init__()
        self._user_input_validation = UserInputValidation()

    @staticmethod
    def get_manager_password(wrong=False):
        msg = "Please enter manager password: "
        if wrong:
            password = input(f"Wrong! {msg}").strip()
        else:
            password = input(msg).strip()
        return password

    def get_action(self):
        msg = "Please choose 1 of the following actions:\n(1) Add Route\n(2) Delete Route\n(3) Update Route\n" \
              "(4) Add Scheduled Ride\nYour choice (1, 2, 3 or 4): "
        while True:
            try:
                action = input(msg).strip()
                valid_action = self._user_input_validation.valid_manager_action(action)
                break
            except WrongManagerAction as e:
                print(f"\n{e}\n")
        return valid_action




if __name__ == '__main__':
    m = ManagerMenu()
    m.get_action()
