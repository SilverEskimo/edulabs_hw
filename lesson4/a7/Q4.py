# In which sublist are there the maximum number of vowels? Print its index.

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
        'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

vowels = ("a", "o", "u", "e", "y", "i")

current_count = 0
prev_count = 0
has_more_vowels = 0

for i, good in enumerate(goods):
    for j, fruit in enumerate(good):
        for char in range(len(fruit)):
            if fruit[char].lower() in vowels:
                current_count += 1
    if current_count > prev_count:
        has_more_vowels = i
    prev_count = current_count
    current_count = 0

print(f'The index of the variable that has more vowels is: {has_more_vowels}')
