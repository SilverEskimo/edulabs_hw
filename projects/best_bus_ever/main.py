import os
import pickle
from best_bus_ever.src.frontend.menu.menu import Menu
from best_bus_ever.src.utils.main_utils import MainUtils
from best_bus_ever.src.backend.best_bus_company import BestBusCompany

if __name__ == '__main__':
    if not os.path.exists('bus_company.pickle'):
        bus_company = BestBusCompany()
    else:
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)
    mu = MainUtils(bus_company)
    while True:
        role = Menu.get_user_role()
        if role == 1:
            mu.password()
            mu.manager_action()
        elif role == 2:
            mu.passenger_action()
        elif role == 3:
            print("Thank you. Bye Bye!")
            bus_company.save_data()
            exit(0)










