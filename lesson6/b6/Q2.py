# Write a program that has 2 modes: insert mode and lookup mode.
# The program asks the user whether he wants to insert a birthday date or to look up a birthday.
# If the user chooses to insert a new date, ask for the person's name and then ask for the person's birthday,
# and store them.If the user chooses lookup mode, ask for a name and return the birthday of the person.
# Divide your program into functions. At least create one function for each command.

birthdays = {}


def get_input():
    while True:
        command = input("Welcome to the birthday dictionary!"
                        "Do you want to insert a new birthday or to lookup one?\n"
                        "'insert' to insert, 'lookup' to lookup & 'quit' to exit: ").strip()
        if command.lower() not in ("insert", "lookup", "quit", "exit"):
            print("Wrong command. Please try again.")
        else:
            return command


def insert_birthday(name: str) -> None:
    confirm = ""
    if birthdays.get(name.lower()):
        confirm = input("We already have this name, do you want to overwrite? (y/n): ").strip()
    if confirm.lower() != "n":
        birth_date = input("Please enter the birthday date: ").strip()
        birthdays[name.lower()] = birth_date
        print("Done!")
    else:
        print("Will not overwrite!")
        return


def lookup_birthday() -> None:
    name_to_lookup = get_name().lower()
    if birthdays.get(name_to_lookup):
        print(f"{name_to_lookup.title()}'s birthday is on {birthdays[name_to_lookup]}")
    else:
        print(f"We do not have {name_to_lookup.title()} in our records")


def get_name() -> str:
    name = input("Please enter the name: ").strip()
    return name


while True:
    user_input = get_input()
    if user_input.lower() in ["quit", "exit"]:
        print("Bye-bye")
        break
    elif user_input.lower() == "insert":
        insert_birthday(get_name())
    elif user_input.lower() == "lookup":
        lookup_birthday()



