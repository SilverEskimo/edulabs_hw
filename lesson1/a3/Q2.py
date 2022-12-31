#Get an integer number from the user and print the amount of digits in the number.
#Assume that the number is in range between 1 and 4000

number = int(input("Please enter a number between 1 and 4000: "))
if number / 1000 >= 1:
    print("The number has 4 digits")
elif number / 100 >= 1:
    print("The number has 3 digits")
elif number / 10 >= 1:
    print("The number has 2 digits")
else:
    print("The number has 1 digit")
