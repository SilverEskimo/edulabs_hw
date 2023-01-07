# Implement a program that helps users to count how many glasses of water they drink every day.
# Your program should support the following actions:
# Add new user by username (signup)
# Allow users to insert number of glasses of water in specific date
# Given the username and specific date, display the user how many glasses of water he drank in that day

users_list = {}


def check_name(name) -> bool:
    if users_list.get(name):
        return True
    return False


def check_date(name, date) -> bool:
    if users_list.get(name, {}).get(date):
        return True
    return False


def get_name():
    return input("Please enter your user name ('quit' for exit): ").strip()


def get_date(total=False):
    msg = "('quit' for exit): "
    if total:
        msg = "('total' for total history, 'quit' for exit): "
    return input("Please enter the date in the following format dd/mm/yy " + msg).strip()


def display_water_data():
    msg = "Exiting display water data"
    while True:
        name = get_name()
        if check_name(name):
            while True:
                date = get_date(total=True)
                if date == 'total':
                    print(f"In total, across all entered dates you have drank {users_list.get(name)['total']} "
                          f"cups of water")
                    break
                elif check_date(name, date):
                    cups_of_water = users_list.get(name).get(date)
                    print(f"On {date} you have drank {cups_of_water} cups of water")
                    break
                elif date == "quit":
                    print(msg + f" for {name}")
                    break
                else:
                    print(f"There is no water data for {date}")
        elif name == "quit":
            print(msg)
            break
        else:
            print(f"There's no such user: {name}")


def register_user():
    while True:
        name = get_name()
        if name == 'quit':
            print("Exiting user signup")
            break
        elif not check_name(name):
            users_list[name] = {"total": 0}
            print(f"User {name} was registered successfully")
            proceed = input(f"Do you want to proceed to entering the data for {name}? (y/n): ").strip()
            if proceed == 'y':
                enter_watter_glasses(name)
            break
        else:
            print("The user already exists, try again or 'quit'")


def enter_watter_glasses(name=""):
    msg = "Exiting enter water data"
    if name == "":
        name = get_name()
    while True:
        if name != "quit":
            date = get_date()
            if date != "quit":
                num_of_cups = int(input("Please enter the number of cups of water for this date: ").strip())
                users_list.get(name)[date] = num_of_cups
                users_list.get(name)["total"] += int(num_of_cups)
            else:
                print(msg + f" for {name}")
                break
        else:
            print(msg)
            break


while True:
    user_input = input("Do you want to sign-up, enter water data or display water data?"
                       "('signup'/'enter'/'display'/'quit'): ").strip()
    if user_input == "signup":
        register_user()
    elif user_input == "enter":
        enter_watter_glasses()
    elif user_input == 'display':
        display_water_data()
    elif user_input == "quit":
        print("Bye Bye")
        break
    else:
        print("Wrong input. Please try again!")