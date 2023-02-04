from best_bus_ever.src.exceptions import *


class UserInputValidation:
    def __init__(self):
        self._value_error_msg = "has to be a number"
        self._err_msg = "Error"

    def valid_role_choice(self, choice: str):
        try:
            role = int(choice)
        except ValueError as e:
            raise WrongUserRoleChoice(f"{self._err_msg}: role {self._value_error_msg}")
        if role != 1 and role != 2:
            raise WrongUserRoleChoice(f"{self._err_msg}: role has to be 1 or 2")
        return role

    def valid_manager_action(self, action: str):
        try:
            user_action = int(action)
        except ValueError as e:
            raise WrongManagerAction(f"{self._err_msg}: manager action {self._value_error_msg}")
        if not 1 <= user_action <= 4:
            raise WrongManagerAction(f"{self._err_msg}: manager action has to be 1 or 2 or 3 or 4")
        return user_action

    def valid_passenger_action(self, action: str):
        try:
            user_action = int(action)
        except ValueError as e:
            raise WrongPassengerAction(f"{self._err_msg}: passenger action {self._value_error_msg}")
        if user_action != 1 and user_action != 2:
            raise WrongPassengerAction(f"{self._err_msg}: passenger action has to be 1 or 2")
        return user_action

    def valid_line_number(self, line_numer: str):
        try:
            line = int(line_numer)
        except ValueError as e:
            raise WrongLineNumber(f"{self._err_msg}: line number {self._value_error_msg}")
        return line

    def valid_scheduled_rides(self, rides: str):
        try:
            rides_list = rides.split(",")
            for i, ride in enumerate(rides_list):
                rides_list[i] = ride.strip()
        except ValueError as e:
            raise WrongScheduledRideFormat(f"{self._err_msg}: rides should be separated by comma")
        return rides_list

