from abc import ABC, abstractmethod
from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class Menu(ABC):
    def __init__(self):
        pass

    welcome = \
        """
          ____            _     ____              ______              
         |  _ \          | |   |  _ \            |  ____|             
         | |_) | ___  ___| |_  | |_) |_   _ ___  | |____   _____ _ __ 
         |  _ < / _ \/ __| __| |  _ <| | | / __| |  __\ \ / / _ \ '__|
         | |_) |  __/\__ \ |_  | |_) | |_| \__ \ | |___\ V /  __/ |   
         |____/ \___||___/\__| |____/ \__,_|___/ |______\_/ \___|_|   
        """

    @classmethod
    def get_user_role(cls):
        print(cls.welcome)
        msg = "Please choose your role:\n" \
              "(1) Manager\n" \
              "(2) Passenger\n" \
              "(3) Exit\n" \
              "Your choice (1, 2 or 3): "
        while True:
            role_str = input(msg).strip()
            try:
                role = UserInputValidation.valid_role_choice(role_str)
                break
            except WrongUserRoleChoice as e:
                print(f"\n{e}\n")
        return role

    @staticmethod
    def get_line_number():
        msg = "Please enter the line number: "
        while True:
            try:
                line_number = input(msg).strip()
                line = UserInputValidation.valid_line_number(line_number)
                break
            except WrongLineNumber as e:
                print(f"\n{e}\n")
        return line

    @staticmethod
    def get_destination():
        return input("Enter destination name: ").strip()

    @staticmethod
    def get_origin():
        return input("Enter origin name: ").strip()

    @staticmethod
    def get_stops():
        return input("Please enter a list of stops separated by space: ").strip()

    @staticmethod
    def get_stop():
        return input("Please enter a bus stop: ").strip()

    @abstractmethod
    def get_action(self):
        pass

