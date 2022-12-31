# Ask the user for a number.Print out whether the number is even or odd.
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')