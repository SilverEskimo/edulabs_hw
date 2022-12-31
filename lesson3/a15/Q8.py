# Given a list with elements of various types, create a new list that will store only positive integers. Print the list.
# For example, for the list:
# various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# The expected output is:
# [5, 2654]

various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
integers = []
for var in various:
    if isinstance(var, bool):
        pass
    elif isinstance(var, int) and var > 0:
        integers.append(var)
print(integers)