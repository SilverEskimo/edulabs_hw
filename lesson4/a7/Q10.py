# Create a single list from the nested lists

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'
            ]
]


new_list = []
count = 0
for good in goods:
    for fruit in good:
        new_list.append(fruit)
        count += len(fruit)
print(f"There are {count} letters in the new list:\n{new_list}")
