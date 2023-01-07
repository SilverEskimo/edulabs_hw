coffee_list = ["Espresso", "Doppio", "Lungo", "Ristretto", "Macchiato", "Corretto", "Con Panna", "Romano", "Cappucino",
               "Americano", "Cafe Latte", "Flat White", "Marocchino", "Mocha", "Bicerin", "Breve", "Raf Coffee",
               "Mead Raf", "Vienna Coffe", "Chocolate Milk", "Latte Macchiato", "Glace", "Freddo", "Irish Coffee",
               "Frappe", "Cappuccino Freddo", "Caramel Frappe", "Espresso Laccino"]

user_input = input("Please enter the time in 24h format (hh:mm) and the number of friends drinking "
                   "together (enter 1 if you're alone)\n(For example - 11:00 3): ").strip().split(" ")
while (len(user_input) < 2 or len(user_input[0]) != 5 or user_input[0][2] != ":" or int(user_input[0][:2]) > 24 \
       or int(user_input[0][3:]) > 59) or int(user_input[1]) < 1:
    user_input = input("Wrong input, please try again: ").strip().split(" ")


starting_number = input("Please enter the coffee number to start with (1 is the first): ").strip()
while not starting_number.isdigit() or int(starting_number) < 1:
    starting_number = input("Wrong input, please try again: ")

coffees_to_skip = input("Please enter the numbers of the coffees to skip (with space in between): ").strip().split(" ")

hour = int(user_input[0][:2])
minute = int(user_input[0][3:])
num_of_people = int(user_input[1])

coffee_per_person = []
coffees_after_skip = []
coffee_list_len = len(coffee_list)
num_of_coffee_to_drink = 0
skip_coffees = False

if coffees_to_skip[0]:
    for i, coffee in enumerate(coffees_to_skip):
        coffees_to_skip[i] = int(coffee) - 1
    for i, coffee in enumerate(coffee_list):
        if i not in coffees_to_skip:
            coffees_after_skip.append(coffee)
    coffee_list_len = len(coffees_after_skip)
    skip_coffees = True

last_person_coffee = hour + int(starting_number) - 2
for i in range(num_of_people):
    if i == 0:
        num_of_coffee_to_drink = last_person_coffee
    else:
        num_of_coffee_to_drink = (last_person_coffee + minute) % coffee_list_len
        last_person_coffee = num_of_coffee_to_drink

    coffee_per_person.append(coffees_after_skip[num_of_coffee_to_drink]) if skip_coffees \
        else coffee_per_person.append(coffee_list[num_of_coffee_to_drink])

for i, coffee in enumerate(coffee_per_person):
    print(f"Person {i + 1} should get the following coffee"
          f": {coffee}")
