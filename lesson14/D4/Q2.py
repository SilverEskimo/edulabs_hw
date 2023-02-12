# Implement a function that filters out vowels from the given string and returns the original string without
# the vowels. Vowels are the following letters (both lowercase and uppercase): a, e,  i, o, u
# Use filter() to filter vowels from a given word (string)

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")


if __name__ == '__main__':
    word = "Process finished with EXit code 0"
    res = filter(lambda char: char not in vowels, word)
    print("".join(res))
