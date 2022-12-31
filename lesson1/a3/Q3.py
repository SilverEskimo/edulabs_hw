#Get 3 numbers as input and print them from the smallest to biggest
#Input example:10 3 83
#Output example: 3 10 83

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

smallest = 0
biggest = 0
medium = 0

if (num1 > num2 > num3) or (num1 > num3 > num2):
    biggest = num1
    if num2 > num3:
        medium = num2
        smallest = num3
    else:
        medium = num3
        smallest = num2
elif (num2 > num1 > num3) or (num2 > num3 > num1):
    biggest = num2
    if num1 > num3:
        medium = num1
        smallest = num3
    else:
        medium=num2
        smallest=num3
elif (num3 > num1 > num2) or (num3 > num2 > num1):
    biggest = num3
    if num1 > num2:
        medium = num1
        smallest = num2
    else:
        medium = num2
        smallest = num1
print(smallest, medium, biggest)