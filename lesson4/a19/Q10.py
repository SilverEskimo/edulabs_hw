#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num * 2):
    if row < num:
        for space in range(1, num - row + 1):
            print(" ", end="")
        for star in range(1, row + 1):
            print("*", end="")
    else:
        for space in range(row - num):
            print(" ", end="")
        for star in range(1, num * 2 - row + 1):
            print("*", end="")
    print("")