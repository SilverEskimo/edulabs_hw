relative_path = "alice.txt"

count = 0
with open(relative_path, mode='r') as my_file:
    for line in my_file:
        count += line.lower().count("alice")
print(f"The string 'alice' appears: {count} times in this file")
