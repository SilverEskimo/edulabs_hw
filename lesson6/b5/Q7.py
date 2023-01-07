# Create a function that receives 2 lists and returns output (choose the right single type) with unique elements
# from list #1 that are absent in list #2
# Case insensitive

colors_1 = ['orange red', 'blue navy', 'BLUE pure', 'snow white', 'sky blue', 'pure purple', 'white cream',
            'Eggshell white', 'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz', 'white & Red', 'sky blue', 'Pale purple',
            'Orchid purple', 'BLUE pure']


def list_to_lower_set(some_list: list) -> set:
    lower_set = set()
    for var in some_list:
        lower_set.add(var.lower())
    return lower_set


def return_unique_absent(list_one: list, list_two: list) -> set:
    set_one = list_to_lower_set(list_one)
    set_two = list_to_lower_set(list_two)

    return set_one.difference(set_two)


print(return_unique_absent(colors_1, colors_2))