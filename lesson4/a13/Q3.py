# Write a program that receives a list of numbers, and finds the second-largest number

numbers = [3, 123, 4443, 12313, 4, 4, 4, 5]

largest = numbers[-1]
second_largest = numbers[1]

if len(numbers) == 0 or numbers.count(numbers[0]) == len(numbers):
    print("All the vars are the same!")
    exit(0)

if second_largest > largest:
    temp = largest
    largest = second_largest
    second_largest = temp

for n in numbers:
    if second_largest < n < largest:
        second_largest = n
    elif second_largest < largest < n:
        second_largest = largest
        largest = n

print(second_largest)