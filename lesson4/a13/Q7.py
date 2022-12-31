# Write a program that receives a number from a user and prints a multiplication table of a given number. For example:
#   Insert a number: 5
#   1*5 = 5
#   2*5 = 10
#   3*5 = 15
#   .
#   .
#   .

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Wrong input, please try again: ")

for i in range(1, 11):
    print(f'{str(i).rjust(2," ")}*{user_num} = {i * int(user_num)}')