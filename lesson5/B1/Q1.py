def sum_of_numbers(numbers: list) -> float:
    res: float = 0
    for number in numbers:
        res += number
    return res


nums: list = [1, 5, 2, 10, 20, 30]
print(sum_of_numbers(nums))

