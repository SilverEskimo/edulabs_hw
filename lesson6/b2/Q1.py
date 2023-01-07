# Write a function to drop empty or None items from a given Dictionary.
# The function should receive 2 arguments - original dictionary and additional optional argument
# “inplace” with default value False.
# If inplace is True, then you should alter the original dictionary.
# Otherwise, you should not alter the original dictionary, but rather you should
# create a new dictionary without empty elements.
# For example:
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': “”,}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
from pprint import pprint
import copy

original_dict = {
    'c1': 'Red',
    'c2': 'Green',
    'c3': None,
    'c4': [],
    'c5': ''
}


def remove_empty_or_none_items(keys_to_remove: list, some_dict: dict):
    for key_to_remove in keys_to_remove:
        some_dict.pop(key_to_remove)
    return some_dict


def check_for_empty_or_none(some_dict: dict):
    empty_items = []
    for key, value in some_dict.items():
        if value is None or not value:
            empty_items.append(key)
    return empty_items


def drop_empty_or_none(some_dict: dict, inplace=False):
    if inplace:
        return remove_empty_or_none_items(check_for_empty_or_none(some_dict), some_dict)
    new_dict = copy.deepcopy(some_dict)
    return remove_empty_or_none_items(check_for_empty_or_none(new_dict), new_dict)


pprint(drop_empty_or_none(original_dict, True))
