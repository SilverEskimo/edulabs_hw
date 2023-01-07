# Implement a function insert_persons that receives int number n as argument, and asks the user to insert the details
# of n persons. The details for each person include: id, first_name, last_name, year, phone.
# The function returns a dictionary with all the persons details while the key of the dictionary is the
# id of a person, and the value is the dictionary that contains the person's details.
from pprint import pprint

person_details_consts = {
    "id": ("ID", int),
    "first_name": ("first name", str),
    "last_name": ("last name", str),
    "birth_year": ("birth year", int),
    "phone_number": ("phone number", str)
}


def insert_one_person(person_num: int) -> dict:
    one_person = {}
    for detail in person_details_consts:
        user_input = input(f"Please enter person's #{person_num} {person_details_consts[detail][0]}: ")
        one_person[detail] = person_details_consts.get(detail)[1](user_input)
    return one_person


def create_people_dict(num_of_people: int) -> dict:
    people_dict = {}
    for person in range(num_of_people):
        person = insert_one_person(person + 1)
        people_dict[person.get("id")] = person
    return people_dict


def get_input() -> dict:
    num_of_people = int(input("Please enter a number of people to add: ").strip())
    return create_people_dict(num_of_people)


pprint(get_input())




