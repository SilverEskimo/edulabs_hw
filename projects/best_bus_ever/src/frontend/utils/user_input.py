from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.frontend.menu.manager_menu import ManagerMenu
from best_bus_ever.src.frontend.menu.passenger_menu import PassengerMenu


class UserInput:
    def __init__(self):
        self._manager_menu = ManagerMenu()
        self._menu = Menu()
        self._passenger_menu = PassengerMenu()

    def get_user_role(self):
        return self._menu.get_user_role()

    def get_manager_action(self):
        return self._manager_menu.get_action()

    def get_manager_password(self, wrong=False):
        if wrong:
            return self._manager_menu.get_manager_password(wrong)
        else:
            return self._manager_menu.get_manager_password()

    def get_passenger_action(self):
        return self._passenger_menu.get_action()

    def get_line_number(self):
        return self._menu.get_line_number()

    def get_scheduled_rides(self):
        return self._menu.get_scheduled_rides()

    def get_destination(self):
        return self._menu.get_destination()

    def get_origin(self):
        return self._menu.get_origin()

    def get_stops(self):
        return self._menu.get_stops()






