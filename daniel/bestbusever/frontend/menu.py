import datetime


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
        stop_list = input("Please insert stop stations separated by comma's: ")
        return stop_list.split(",")

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
        o_t = input("Insert origin time in format 'hh-mm':  ")
        converted_orig = datetime.datetime.strptime(o_t, "%H-%M")
        return converted_orig.time()

    @staticmethod
    def get_driver():
        return input("Driver's Name? ")

    @staticmethod
    def get_dest_time():
        d_t = input("Insert destination time in format 'hh-mm':  ")
        converted_dest = datetime.datetime.strptime(d_t, "%H-%M")
        return converted_dest.time()

    @staticmethod
    def search_by():
        return int(input("By what do you wanna search?\n"
                         "1.Line number \n"
                         "2.Origin \n"
                         "3.Destination \n"
                         "4.Stop \n"
                         " "))


