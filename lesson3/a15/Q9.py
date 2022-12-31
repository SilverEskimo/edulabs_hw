# Write a program to count the number of even and odd numbers from a given list of numbers.

num_list = [1, 2, 3, 4, 5, 6, 7]

count_even = 0
for number in num_list:
    if number % 2 == 0:
        count_even += 1
print(f"The number of even numbers is: {count_even}\n"
      f"The number of odd numbers is: {len(num_list) - count_even}")
