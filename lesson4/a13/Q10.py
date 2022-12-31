# Write a program that receives a number from a user and prints the following start pattern.
# For example, for input 5, you should print:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

num = input("Please enter a number: ").strip()
while not num.isdigit() or int(num) <= 0:
    num = input("Wrong input, please try again: ")

for row in range(1, int(num) + 1):
    for col in range(1, row + 1):
        print("*", "", end="")
    print("")

for row in range(int(num) - 1, 0, -1):
    for col in range(row, 0, -1):
        print("*", "", end="")
    print("")