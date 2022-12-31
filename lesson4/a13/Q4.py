# Print list in reverse order using a for loop

nums_list = [10, 20, 32, 1, 3, 5]

list_len = len(nums_list)
for i in range(list_len - 1, -1, -1):
    print(nums_list[i])