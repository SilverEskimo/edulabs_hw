# Write a program that receives a list of numbers, and prints the minimum number

nums_list = [10, 20, 32, 1, 3, 5]

min_var = nums_list[0]

for num in nums_list:
    if num < min_var:
        min_var = num

print("The minimal number is:", min_var)