# Add  ‘2’ to every second word in each list (pear ⇒ pear2, chery ⇒chery2)

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
            ]
]

for good in goods:
    for fruit in range(1, len(good), +2):
        good[fruit] += '2'

print(goods)
