# Write a program to display all prime numbers within a range provided by the user.
# Note: A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

user_num = input("Please enter a number: ").strip()

while not user_num.isdigit() or int(user_num) <= 1:
    user_num = input("Wrong input, please try again: ")

prime_nums = []
for num in range(2, int(user_num)):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        prime_nums.append(num)
if prime_nums:
    print(prime_nums)
else:
    print(f"There are no prime numbers before: {user_num}")



