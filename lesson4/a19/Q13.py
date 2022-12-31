#     *
#    * *
#   *   *
#  *     *
# *********

user_num = input("Please enter a number: ").strip()
while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num + 1):
    if row == 1:
        for col in range(1, num + row):
            if col == num:
                print("*", end="")
            else:
                print(" ", end="")
    elif row == num:
        for col in range (1, num + row):
            print("*", end="")
    else:
        for col in range(1, num * 2):
            if col == num - (row - 1) or col == num + row - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print("")