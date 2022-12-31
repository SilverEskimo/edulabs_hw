# Write a program that receives rows number  and prints the following number pattern:
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5

rows = input("Please enter a number of rows: ").strip()

while not rows.isdigit() or int(rows) <= 0:
    rows = input("Wrong input, please try again: ")

for i in range(1, int(rows) + 1):
    for j in range(1, i + 1):
        print(i, "", end="")
    print("")