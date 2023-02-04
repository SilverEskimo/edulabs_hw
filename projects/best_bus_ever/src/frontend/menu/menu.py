from abc import abstractmethod
from best_bus_ever.src.exceptions import *
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class Menu:
    def __init__(self):
        self._user_input_validation = UserInputValidation()
        self._welcome = \
"""
  ____            _     ____              ______              
 |  _ \          | |   |  _ \            |  ____|             
 | |_) | ___  ___| |_  | |_) |_   _ ___  | |____   _____ _ __ 
 |  _ < / _ \/ __| __| |  _ <| | | / __| |  __\ \ / / _ \ '__|
 | |_) |  __/\__ \ |_  | |_) | |_| \__ \ | |___\ V /  __/ |   
 |____/ \___||___/\__| |____/ \__,_|___/ |______\_/ \___|_|   
"""

    def get_user_role(self):
        print(self._welcome)
        msg = "Please choose your role:\n(1) Manager\n(2) Passenger\nYour choice (1 or 2): "
        while True:
            role_str = input(msg).strip()
            try:
                role = self._user_input_validation.valid_role_choice(role_str)
                break
            except WrongUserRoleChoice as e:
                print(f"\n{e}\n")
        print(role)
        return role

    def get_line_number(self):
        msg = "Please enter the line number: "
        while True:
            try:
                line_number = input(msg).strip()
                line = self._user_input_validation.valid_line_number(line_number)
                break
            except WrongLineNumber as e:
                print(f"\n{e}\n")
        return line

    def get_scheduled_rides(self):
        msg = "Please the scheduled rides in the following format: dd/mm/yyyy hh:mm separated by comma: "
        while True:
            try:
                rides = input(msg).strip()
                valid_rides = self._user_input_validation.valid_scheduled_rides(rides)
                break
            except WrongScheduledRideFormat as e:
                print(f"\n{e}\n")
        return valid_rides

    @staticmethod
    def get_destination():
        return input("Enter destination name: ").strip()

    @staticmethod
    def get_origin():
        return input("Enter origin name: ").strip()

    @staticmethod
    def get_stops():
        return input("Please enter a list of stops separated by space: ")

    @abstractmethod
    def get_action(self):
        pass


if __name__ == '__main__':
    m = Menu()
    m.get_user_role()
