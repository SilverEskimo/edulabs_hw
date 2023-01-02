id_num = input("Please enter an id number: ").strip()
while not id_num.isdigit() or len(id_num) != 9:
    id_num = input("Wrong input, please try again: ")


id_str_wo_check = id_num[:-1]
check_digit = int(id_num) % 10

res_of_mult = 0
res_to_calc = 0

for char in range(len(id_str_wo_check) - 1, -1, -1):
    last_digit = id_str_wo_check[-1]
    if char % 2 != 0:
        res_of_mult = int(last_digit) * 2
        while res_of_mult > 9:
            res_of_mult = int(str(res_of_mult)[0]) + int(str(res_of_mult)[1])
    else:
        res_of_mult = int(last_digit)
    id_str_wo_check = id_str_wo_check[:-1]
    res_to_calc += res_of_mult
    res_of_mult = 0

if 10 - (res_to_calc % 10) == check_digit:
    msg = "valid"
else:
    msg = "invalid"

print(f"The entered ID is {msg}")