# Implement a function second_largest that receives a list of numbers and returns the
# second-largest number in the list.
# You can assume that there are no non-numeric values in the list.
# You are not allowed to use any built-in function like sort() / sorted() / min() / max() or similar!
nums_list = [54, -1, 45, 987, 5, 2, 65, 7, 12]


def find_second_largest(nums: list) -> float | None:
    if not nums:
        return None

    temp = 0
    largest = nums[-1]
    second_largest = nums[0]

    if second_largest > largest:
        temp = second_largest
        second_largest = largest
        largest = temp

    for num in nums:
        if second_largest <= num < largest:
            second_largest = num
        elif second_largest < largest < num:
            second_largest = largest
            largest = num
        elif num <= largest < second_largest:
            temp = second_largest
            second_largest = largest
            largest = temp
    return second_largest


print(find_second_largest(nums_list))
