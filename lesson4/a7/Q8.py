# Reverse every word that includes the letter “p”, and store the reverse version in a new list. Print the list.

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry'
            ]
]


p_reversed_list = []
reversed_fruit = ""
for good in goods:
    for fruit in good:
        if 'p' in fruit.lower():
            p_reversed_list.append(fruit[-1::-1])
            reversed_fruit = ""

print(p_reversed_list)