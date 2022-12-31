#     *
#    **
#   ***
#  ****
# *****

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")


for row in range(1, int(user_num) + 1):
    for col in range(int(user_num), row, -1):
        print(" ", sep="", end="")
    for star in range(1, row + 1):
        print("*", end="")
    print("")