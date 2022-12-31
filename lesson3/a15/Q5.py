# Find the sum of the series up to n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become:
# 2 + 22 + 222 + 2222 + 22222 = 24690

user_input = input("Please enter a number: ").strip()

while not user_input.isdigit() or int(user_input) < 1:
    user_input = input("Wrong input, please try again: ").strip()

series_sum = 2
print(series_sum, end="")
for i in range(2, int(user_input)+1):
    print(" +", str(2) * i, end="")
    series_sum += int(str(2) * i)

print(f" = {series_sum}")