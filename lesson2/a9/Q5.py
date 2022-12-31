# Implement a code that receives the layout of the seats in the aircraft as letters and returns the layout as numbers. For example:
# ABC DEF => 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.

layout1 = input("Please enter the first batch of the layout of the seats in your aircraft: ")
layout2 = input("Please enter the second batch of the layout of the seats in your aircraft: ")
layout3 = input("Please enter the third batch of the layout of the seats in your aircraft: ")

if layout1 != "" and layout2 != "" and layout3 != "":
    print(f'{len(layout1)}:{len(layout2)}:{len(layout3)}')
elif layout1 != "" and layout2 != "":
    print(f'{len(layout1)}:{len(layout2)}')
elif layout1 != "":
    print(f'{len(layout1)}')
else:
    print("This is a very strange plane :)")

