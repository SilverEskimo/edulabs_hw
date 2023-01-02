# Write a Python function to create and print a list where the values are
# square of numbers between 1 and 30 (both included)

def print_squares():
    list_of_squares = []
    for num in range(1, 31):
        list_of_squares.append(num**2)
    for num in list_of_squares:
        print(num, end=" ")


print_squares()