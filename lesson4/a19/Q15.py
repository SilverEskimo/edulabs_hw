#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

user_num = input("Please enter a number: ").strip()
while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num * 2):
    if row == 1 or row == num * 2 - 1:
        for space in range(1, num):
            print(" ", end="")
        print("*", end="")
    elif row <= num:
        for col in range(1, num * 2):
            if col == num - (row - 1) or col == num + row - 1:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for col in range(1, num * 2):
            if col == (row - num) + 1 or col == num * 2 - (row - num) - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print("")