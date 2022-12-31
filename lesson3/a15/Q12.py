# Write a program that receives as input 2 numbers - rows and columns, and prints a rectangle of $ with received dimensions.
# For example, for the following input:
# Rows: 5, Columns: 3
# The expected output is:
# $$$
# $$$
# $$$
# $$$
# $$$

rows = int(input("Please enter the number of rows: ").strip())
cols = int(input("Please enter the number of columns: ").strip())

for i in range(rows):
    print('$' * cols)