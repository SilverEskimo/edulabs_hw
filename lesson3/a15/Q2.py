# Use a loop to display elements from a given list present at odd index positions.
# For example, for list:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output is:
# 20 40 60 80 100
# For example, for list:
# my_list = [56, 32, 1, -9, 78, 46, -8, 9, 2, 7]
# Expected output is:
# 32 -9 46 9 7

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i], end=" ")


