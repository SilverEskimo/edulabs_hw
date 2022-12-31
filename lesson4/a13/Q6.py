# Find the factorial of a given number.
# Take into account that factorial of 0 is 1, and factorial does not exist for negative numbers.
num = 7
factorial_res = 1
if num >= 0:
    for i in range(1, num + 1) :
        factorial_res *= i
else:
    print("Negative number!")

print(factorial_res)