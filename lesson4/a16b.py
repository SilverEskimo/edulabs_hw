# Shows the instructions on how to use it.
# The application will randomly fit the remaining numbers
# 0 digits entered ⇒ application will generate all numbers
# 1-8 digits entered by user ⇒ application will generate the remaining digits
# More than 8 digits entered ⇒ application will reference only first 8
# Interesting use case:
# Use your birth date: March 2, 1993 => 02031993 ⇒application returns 020319933
import random


id_num = input("This program generates a random valid ID number. You can enter up to 8 digits to start with or empty "
                f"for a completely random ID number: ").strip()

while (id_num != "" and not id_num.isdigit()) or len(id_num) > 8:
    id_num = input("Wrong input, please try again: ")

res_of_sum = 0
res_to_calc = 0

if len(id_num) == 0:
    id_num = ""
    for num in range(8):
        id_num += str(random.randint(0, 9))
elif 0 < len(id_num) <= 8:
    for num in range(8 - len(id_num)):
        id_num += str(random.randint(0, 9))

id_to_trim = id_num

for char in range(len(id_num) - 1, -1, -1):
    last_digit = id_to_trim[-1]
    if char % 2 != 0:
        res_of_mult = int(last_digit) * 2
        while res_of_mult > 9:
            res_of_mult = int(str(res_of_mult)[0]) + int(str(res_of_mult)[1])
    else:
        res_of_mult = int(last_digit)
    id_to_trim = id_to_trim[:-1]
    res_to_calc += res_of_mult
    res_of_mult = 0

check_digit = 10 - res_to_calc % 10
id_num += str(check_digit)
print(f"Your new ID number is: {id_num}")
