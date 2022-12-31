# Write a program that receives an integer number from a user and appends squares of the numbers starting
# from 1 up to the number inserted by a user to a new list. Print the new list with the squares.

user_input = input("Please enter a number: ").strip()
while not user_input.isdigit() or int(user_input) < 1:
    user_input = input("Wrong input, please try again: ").strip()

sqr_list = []
for i in range(1, int(user_input)):
    sqr_list.append(i**2)

print(sqr_list)