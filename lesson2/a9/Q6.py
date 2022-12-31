# Implement a code that receives the aircraft seat number (4J, 34A, etc…) and aircraft layout like in the previous exercise (ABC DEF, ABC DEFGH IJK,...)
# Your code should print out 3 things:
# Row number
# Seat Character
# Print whether the user is going to sit near the window, in the aisle, or in the middle.
# For example, for the input: 4J and ABC DEFG HIJ: the output should be:
# Row number: 4
#    	Char: J
# Window
#
# You can assume that row number is a maximum 2-digit number, and seat Char is always a one single char.

seat_input = input("Please enter your seat: ").strip().lower()
layout_input = input("Please enter your plane layout: ").strip().lower()

seat_position = "middle"
row_number = seat_input[0] if len(seat_input) == 2 else seat_input[0:2]
seat_char = seat_input[-1]
layout_list = layout_input.split(" ")

if seat_char == layout_input[0] or seat_char == layout_input[-1]:
    seat_position = "window"

if len(layout_list) == 3:
    if seat_char in (layout_list[1][0], layout_list[1][-1], layout_list[0][-1], layout_list[2][0]):
        seat_position = "aisle"
elif len(layout_list) == 2:
    if seat_char in (layout_list[0][-1], layout_list[1][0]):
        seat_position = "aisle"
elif seat_char == layout_list[0][-1]:
    seat_position = "aisle"

print(f'You are going to seat in the {seat_position}\nYour row number is: {row_number}\nAnd the seat char is: \
{seat_char.capitalize()}')