class Menu:


    @staticmethod
    def main_menu():
        user_role = input("Hello. Please choose your role:\n1. Passenger\n2. Manager\nYour choice (1 or 2): ")
        return int(user_role)

    @staticmethod
    def passenger_menu():
        passenger_action = input("Please choose your action:\n1. Search Route\n2. Report Delay\n3. Exit: \n"
                                 "Your Choice: ")
        return int(passenger_action)

    @staticmethod
    def search_route():
        pass

    @staticmethod
    def manager_menu():
        manager_action = input("Please enter your action:\n1. Add Route\n2. Delete Route\n"
                               "3. Update Route\n4. Add Scheduled Ride\n5. Exit \n"
                               "Your Choice: ")
        return int(manager_action)

    @staticmethod
    def get_line_number():
        return int(input("Please enter the line number: ").strip())


    @staticmethod
    def get_origin():
        return str(input("Please enter origin: "))

    @staticmethod
    def get_list_stop():
        return input("Please insert stop stations separated by comma's: ")

    @staticmethod
    def get_destination():
        return str(input("Please insert destination stop: "))


    @staticmethod
    def delete_route():
        return int(input("What route do you want to delete? "))

    @staticmethod
    def update_route():
        return input("What do you want to update in this line?\n"
                         "1. Origin \n"
                         "2. Destination \n"
                         "3. List of Stops ")

    @staticmethod
    def get_info():
        return int(input("What line number would you like to update with a new ride? "))

    @staticmethod
    def get_origin_time():
        return input("Origin Time? ")

    @staticmethod
    def get_driver():
        return input("Driver's Name? ")

    @staticmethod
    def get_dest_time():
        return input("Destination Time? ")


