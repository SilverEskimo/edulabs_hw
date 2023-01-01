# Print all the words that include more than 5 letters


goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'
            ]
]

for good in goods:
    for fruit in good:
        if len(fruit) >= 5:
            print(fruit, end=" ")