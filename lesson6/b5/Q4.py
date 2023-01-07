# Create a function that receives 3 lists and returns output (choose the right single type) that will indicate which
# colors are derived from basic colors. Basic colors are ones stored in colors_0. Others are derived colors.
# Case insensitive

colors_0 = ['red', 'blue', 'Purple', 'white']
colors_1 = ['orange red', 'blue navy', 'BLUE pure', 'snow white', 'sky blue', 'pure purple', 'white cream',
            'Eggshell white', 'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz', 'white & Red', 'sky blue', 'Pale purple', 'Orchid purple',
            'BLUE pure', "black rose"]


def list_to_lower_set(some_list: list) -> set:
    lower_set = set()
    for var in some_list:
        lower_set.add(var.lower())
    return lower_set


def find_derived(basic_list: list, list_one: list, list_two: list):
    res_set = set()
    set_one = list_to_lower_set(list_one)
    set_two = list_to_lower_set(list_two)
    unified_list = list(set_one.union(set_two))
    for index in range(len(basic_list)):
        basic_list[index] = basic_list[index].lower()
    for var in unified_list:
        color_split = var.split(" ")
        for color in color_split:
            if color in basic_list:
                res_set.add(var)
    return res_set


print(find_derived(colors_0, colors_1, colors_2))
