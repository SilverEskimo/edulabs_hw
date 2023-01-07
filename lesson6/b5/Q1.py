# flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
# color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# Create a function that receives 2 lists and returns a dictionary, where
# keys are elements from the list #1 and values are elements from the list #2.
# Assume: number of elements in both lists are equal
# Don’t lose any information

from pprint import pprint

flowers = ['Rose', 'Lily', 'Tulip', 'Orchid', 'Carnation', 'Hyacinth', 'Rose']
color = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']


def convert_to_dict(list_one: list, list_two: list) -> dict:
    res_dict = {}

    for index in range(len(list_one)):
        key = list_one[index]
        value = list_two[index]
        if res_dict.get(key.lower(), {}):
            res_dict.get(key.lower()).append(value)
        else:
            res_dict[key.lower()] = [value]
    return res_dict


pprint(convert_to_dict(flowers, color))
