# Find the shortest words
# Find the exact indexes (2-number indices)

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
            ]
]

# please note to the 2 cases that are there current > longest AND current = longest
shortest_word = len("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+?><~")
shortest_words = [""]
shortest_indexes = [("", "")]

for i, good in enumerate(goods):
    for j, fruit in enumerate(good):
        if len(fruit) < shortest_word:
            shortest_word = len(fruit)
            shortest_words = [fruit]
            shortest_indexes = [(i, j)]
        elif len(fruit) == shortest_word:
            shortest_words.append(fruit)
            shortest_indexes.append((i, j))

for i, word in enumerate(shortest_words):
    print(f"The shortest word is: {word} and its index is: {shortest_indexes[i]}")