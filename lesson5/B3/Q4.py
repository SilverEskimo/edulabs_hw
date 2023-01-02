# Write a Python function that receives a string as a parameter and calculates
# the number of upper case letters and lowercase letters. (The function should return 2 numbers in a tuple)
from string import ascii_uppercase, ascii_lowercase


def calc_lower_and_upper(word: str) -> tuple[int]:
    lower_count = 0
    upper_count = 0
    for char in word:
        if char in ascii_lowercase:
            lower_count += 1
        else:
            upper_count += 1
    return upper_count, lower_count


print(calc_lower_and_upper("ABaCefLgd"))