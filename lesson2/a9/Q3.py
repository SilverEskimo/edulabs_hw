# Get string as an input, and print out string statistics:
# Amount of words
# Amount of chars
# Amount of non-whitespace chars
# Amount of vowels

user_input = input("Please enter a string: ")

count_vowels = 0
words = user_input.strip().split(" ")
length = len(user_input)
non_whitespace = length - user_input.count(" ")

count_vowels += user_input.count("a")
count_vowels += user_input.count("e")
count_vowels += user_input.count("i")
count_vowels += user_input.count("o")
count_vowels += user_input.count("u")
count_vowels += user_input.count("y")

print(f"Amount of words: {len(words)}\nAmount of chars: {length}\nAmount of non-whitespace: {non_whitespace}\nAmount of vowels: {count_vowels}")