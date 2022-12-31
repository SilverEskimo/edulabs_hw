# Write a code that decides whether a person can ride a roller coaster. You can ride a roller coaster if:
# Your age is between 8 and 18, and your height is at least 115 cm
# If you are more than 18 years old, then the minimum allowed height is 100cm
# Write a code that receives as input person’s age and height, and prints “You can ride” if the person can ride
# the roller coaster, otherwise print: “You cannot ride”

age = int(input("Please enter your age: "))
height = int(input("Please enter your height: "))

if (18 >= age >= 8 and height >= 115) or \
        (age >= 18 and height >= 100):
    print("You can ride")
else:
    print("You cannot ride")

