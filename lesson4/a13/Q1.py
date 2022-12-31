# Write a program that receives a number from a user and calculates the sum of all numbers from 1 to a given number

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Wrong input, please try again: ")

sum_of_prevs = 0
for i in range(1,int(user_num) + 1):
    sum_of_prevs += i
print(sum_of_prevs)

