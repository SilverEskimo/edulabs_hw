# Calculate the cube of all numbers from 1 to a given number.
# For example, for input 6, expected output is:
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

user_input = input("Please enter a number: ").strip()

while not user_input.isdigit() or int(user_input) < 1:
    user_input = input("Wrong input, please try again: ").strip()

for i in range(1, int(user_input) + 1):
    print(f"Current number is: {i} and the cube is {i**3}")
