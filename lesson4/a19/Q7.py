# * * * * *
#  * * * *
#   * * *
#    * *
#     *

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for rows in range(1, num+1):
    for cols in range(1, rows):
        print(" ", end="")
    for stars in range(num, rows - 1, -1):
        print("*", end=" ")
    print("")
