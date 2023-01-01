# Create a single list where all the words are from the “goods” list. For each word in the list:
# Cut last 3 letters
# Add cutted 3 letters to the beginning of the word in the reverse order
# Was ‘apple’ ⇒ ‘ap’ +’ple’ ⇒ ‘ple’ +’ap’ ⇒ ‘elp’ + ‘ap’ ⇒ final result: ‘elpap’

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
            ]
]

new_list = []
last_three_chars = ""
reverse_last_three_chars = ""
word_after_last_three = ""
for good in goods:
    for fruit in good:
        reverse_last_three_chars = fruit[-1:-4:-1]
        last_three_chars = reverse_last_three_chars[-1::-1]
        word_after_last_three = fruit.replace(last_three_chars, "")
        new_list.append(reverse_last_three_chars + word_after_last_three)
print(new_list)





