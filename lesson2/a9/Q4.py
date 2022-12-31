# In this exercise you will get used to reading code documentation, which is an important part of every developer's daily job. Use the following official python string documentation and solve the exercises:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# Receive a word from a user, and print out whether the word ends with a vowel (a, e, i, o, u, y)
# Receive a string from a user, and print out whether the string contains only whitespaces.
# Receive a sentence from a user, and return the same sentence while every word in it starts from uppercase. For example, for the input "The sun is shining", your program should return: "The Sun Is Shining"
VOWELS = ("a", "e", "i", "o", "u", "y")

user_input = input("Please enter a string: ")
is_vowel = "not"

print("Vowel?:", user_input.endswith(VOWELS))
print("Only whitespaces?:", user_input.isspace())
print("Uppercased:", user_input.title())
