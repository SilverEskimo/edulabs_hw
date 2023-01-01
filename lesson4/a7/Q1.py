# Find the longest words
# Find the exact indexes (it should contain 2 numbers - the inner list idx + the string index.)
# For example, the index for ‘durian’ is: (1, 3)
# Find and print the amount of vowels in these words

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'
            ]
]

# please note to the 2 cases that are there current > longest AND current = longest
longest_word = len("")
longest_words = [longest_word]
longest_indexes = [("", "")]

for i, good in enumerate(goods):
    for j, fruit in enumerate(good):
        if len(fruit) > longest_word:
            longest_word = len(fruit)
            longest_words = [fruit]
            longest_indexes = [(i, j)]
        elif len(fruit) == longest_word:
            longest_words.append(fruit)
            longest_indexes.append((i, j))

for i, word in enumerate(longest_words):
    print(f"The longest word is: {word} and its index is: {longest_indexes[i]}")