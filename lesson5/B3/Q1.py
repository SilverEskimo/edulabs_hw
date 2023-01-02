# Write a function that receives a hyphen-separated sequence of words as a parameter and returns a list of words in
# a hyphen-separated sequence after sorting them alphabetically.
# Sample input : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
usr_input = "green-red-yellow-black-white"

def sort_words(words: str) -> list:
    split_list = words.split("-")
    new_list = [split_list[0]]
    temp_word = ""
    for i, word in enumerate(split_list):
        print(new_list)


sort_words(usr_input)