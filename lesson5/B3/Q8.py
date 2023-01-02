# Write a Python function to check whether a number is perfect or not.

def check_if_perfect(number: int) -> bool:
    divisors_list = []
    for num in range(1, number):
        if number % num == 0:
            divisors_list.append(num)
    print(divisors_list)
    if sum(divisors_list) == number:
        return True
    return False

print(check_if_perfect(495))
