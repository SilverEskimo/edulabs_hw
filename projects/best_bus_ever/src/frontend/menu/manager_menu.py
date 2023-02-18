from best_bus_ever.src.utils.utils import Utils
from best_bus_ever.src.utils.exceptions import *
from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.frontend.utils.user_input_validations import UserInputValidation


class ManagerMenu(Menu):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_origin_time():
        return input("\nPlease enter the origin time in the following format hh:mm: ").strip()

    @staticmethod
    def get_destination_time():
        return input("Please enter the destination time in the following format hh:mm: ").strip()

    @staticmethod
    def get_driver_name():
        return input("Please enter the driver's name: ").strip()

    @staticmethod
    def get_manager_password(count, wrong=False):
        msg = "Please enter manager password"
        if wrong:
            password = input(f"Wrong! {msg} ({3-count} attempts left): ").strip()
        else:
            password = input(f"{msg}: ").strip()
        return password

    @staticmethod
    def get_action():
        msg = "Please choose 1 of the following actions:\n(1) Add Route\n(2) Delete Route\n(3) Update Route\n" \
              "(4) Add Scheduled Ride\n(5) Exit\nYour choices (1, 2, 3, 4 or 5): "
        while True:
            try:
                action = input(msg).strip()
                valid_action = UserInputValidation.valid_manager_action(action)
                break
            except WrongManagerAction as e:
                print(f"\n{e}\n")
        return valid_action

    @staticmethod
    def get_update_option():
        msg = "Please choose what you want to update:\n(1) Origin\n(2) Destination\n(3) Stops\n(4) Back to main menu" \
              "\nYour choice (1, 2, 3 or 4. For multiple updates - provide choices separated by space): "
        while True:
            try:
                action = input(msg).strip()
                valid_actions = UserInputValidation.valid_update_actions(action)
                break
            except WrongManagerAction as e:
                print(f"\n{e}\n")
            except WrongUpdateRange as e:
                print(f"\n{e}\n")
        return valid_actions

    def get_scheduled_ride(self):
        while True:
            try:
                origin_time = self.get_origin_time()
                destination_time = self.get_destination_time()
                Utils.convert_ride_times((origin_time, destination_time))
                break
            except WrongTimeFormat as e:
                print(f"\n{e}\n")
        driver_name = self.get_driver_name()
        return origin_time, destination_time, driver_name

