# Write a program that receives a number from a user and constructs the following pattern, using a nested loop. For example, for n=9:
# Expected Output:
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


user_input = input("Please enter a number: ").strip()
while not user_input.isdigit() or int(user_input) < 1:
    user_input = input("Wrong input, please try again: ").strip()

n = int(user_input)

# Single loop
for i in range(1, n + 1):
    print(str(i) * i)

# Nested loop
# for i in range(1, n + 1):
#     row = ""
#     for j in range(1, i + 1):
#         row += str(i)
#     print(row)