# Create a new list with the structure of the original list, but such that all the words will be replaced with
# only 3 first letters of each original word.

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
            ]
]

new_list = []

for i, good in enumerate(goods):
    new_list.append([])
    for fruit in good:
        new_list[i].append(fruit[0:3])

print(new_list)