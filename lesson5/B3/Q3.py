# Write a program that can execute 2 actions (according to user choice): insert and search.
# Insert asks the user to insert a word and stores it.
# Search asks for a letter and a number and from all the words that have been stored before it displays
# only words in which the provided letter appeared exactly number times.
# Divide the program into functions.


def insert_words(usr_input: str) -> list[str]:
    return usr_input.split(" ")


def search_words(usr_insert, usr_search: str) -> list[str]:
    words = insert_words(usr_insert)
    char_to_search , num_of_appearances = user_search.split(" ")
    res_list = []
    for word in words:
        if int(num_of_appearances) == word.count(char_to_search):
            res_list.append(word)
    return res_list


user_insert: str = input("Please insert words separated by space: ").strip()
user_search: str = input("Please enter a letter and a number separated by space: ").strip()

res = search_words(user_insert, user_search)

if res:
    print(res)
else:
    print("There are no words with this number of the requested char")

