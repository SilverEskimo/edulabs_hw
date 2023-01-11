# Implement a function my_sqrt that receives a non-negative integer x, and returns
# the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator like x ** 0.5 or math.sqrt()  in python.



def find_sqr(num: int) -> int:
    count = 1
    while True:
        if count * count == num:
            return count
        elif count*count > num:
            return count - 1
        count += 1


print(find_sqr(15))






