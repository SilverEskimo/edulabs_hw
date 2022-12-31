word = input("Please enter a word: ")

is_pal = ""
if word != word[::-1]:
    is_pal = "not"
print(f'{word} is {is_pal} palindrome')