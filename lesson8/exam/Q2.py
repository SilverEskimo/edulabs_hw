# Implement a functions fizz_buzz that receives an integer num
# and returns list of strings ret_val of length num, such that:
# ret_val[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ret_val[i] == "Fizz" if i is divisible by 3.
# ret_val[i] == "Buzz" if i is divisible by 5.
# ret_val[i] == i (as a string) if none of the above conditions are true.


def fizz_buzz(num: int) -> list[str]:
    res_list = ["1", "2"]
    for i in range(3, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            res_list.append("FizzBuzz")
        elif i % 3 == 0:
            res_list.append("Fizz")
        elif i % 5 == 0:
            res_list.append("Buzz")
        else:
            res_list.append(str(i))
    return res_list


print(fizz_buzz(15))
