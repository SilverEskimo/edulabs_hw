# *********
#  *     *
#   *   *
#    * *
#     *

user_num = input("Please enter a number: ").strip()
while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num + 1):
    if row == 1:
        for col in range(1, num * 2):
            print("*", end="")
    elif row == num:
        for space in range(1, row):
            print(" ", end="")
        print("*", end="")
    else:
        for col in range(1, num * 2):
            if col == row or col == num * 2 - row:
                print("*", end="")
            else:
                print(" ", end="")
    print("")