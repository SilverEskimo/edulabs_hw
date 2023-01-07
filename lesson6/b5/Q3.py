# Lists:
# color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']
# Expected output:
# red, white, blue, purple
# Create a function that receives two lists and returns output (choose the right type)
# that includes colors that exist in both lists
#  - Case insensitive
import copy
from copy import deepcopy

color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']


def list_to_lower_set(some_list: list) -> set:
    lower_set = set()
    for var in some_list:
        lower_set.add(var.lower())
    return lower_set


def return_common_values(list_one: list, list_two: list) -> set:
    set_one = list_to_lower_set(list_one)
    set_two = list_to_lower_set(list_two)
    return set_one.intersection(set_two)


print(return_common_values(color_1, colors_2))
