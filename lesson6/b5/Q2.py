# List:
# colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']
# Create a function that receives a list and returns output (choose the right type) with unique elements only
# No duplicated elements
# Case insensitive
# Expected result: red,white, blue, sky blue, purple, orange with white straps.


colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']


def return_wo_duplicate(some_list: list) -> set:
    res_set = set()
    for var in some_list:
        res_set.add(var.lower())
    return res_set



return_wo_duplicate(colors_2)