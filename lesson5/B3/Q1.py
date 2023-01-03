# Write a function that receives a hyphen-separated sequence of words as a parameter and returns a list of words in
# a hyphen-separated sequence after sorting them alphabetically.
# Sample input : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
usr_input = "green-red-yellow-black-white"

def sort_words(user_input: str) -> str:
    words = user_input.split("-")
    for i in range(len(words)):
        min_index = i
        for j in range(i + 1, len(words)):
            if words[j] < words[min_index]:
                min_index = j
        words[i], words[min_index] = words[min_index], words[i]
    res = words[0]
    for word in range(1, len(words)):
        res += "-" + words[word]
    return res

print(sort_words(usr_input))
