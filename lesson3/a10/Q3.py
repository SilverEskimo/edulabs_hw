count = 0
numbers_sum = 0

numbers = None

while numbers != "$$$":
    msg = "The input is wrong, please try again: "
    if numbers is None:
        msg = "Please enter numbers and end your input with '$$$': "
    elif numbers.isdigit() or numbers == "$$$":
        num = int(numbers)
        numbers_sum += num
        count += 1
        msg = f"Got {numbers}. Next input please: "
    numbers = input(msg).strip()
print(f'The sum is: {numbers_sum}\nThe average is: {numbers_sum/count}')
