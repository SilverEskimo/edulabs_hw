# **
# * *
# ***
# * *
# * *
# * *
user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(1, num):
    for col in range(1, (num // 2) + 1):
        if row == 1:
            if col == 1 or col == num // 2:
                print(" ", end="")
            else:
                print("*", end="")
            # the solution as it was required:
            # if col != (num // 2):
            #     print("*", end="")
        elif row == num // 2:
            print("*", end="")
        else:
            if col == 1 or col == num // 2:
                print("*", end="")
            else:
                print(" ", end="")
    print("")




