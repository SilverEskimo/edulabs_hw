# Find all the words that include letter ‘b’ and store them in a new list. Print the list.
goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
        'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

b_list = []

for good in goods:
    for word in good:
        if 'b' in word:
            b_list.append(word)
print(b_list)

