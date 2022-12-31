# * * * * *
# * * * *
# * * *
# * *
# *

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

num = int(user_num)

for row in range(num, 0, -1):
    for col in range(1, row + 1):
        print("*","", end="")
    print("")