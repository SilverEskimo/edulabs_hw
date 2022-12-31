# *****
#  ****
#   ***
#    **
#     *


user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num + 1):
    for col in range(1, row):
        print(" ", end="")
    for stars in range(num, row - 1, -1):
        print("*", end="")
    print("")