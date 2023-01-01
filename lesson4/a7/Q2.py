# Find indices of words that start with vowels and store them in a new list. Print the list.
goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry',
            ]
]

vowels = ("a", "o", "u", "e", "y", "i")

starts_with_vowel = []

for i, good in enumerate(goods):
    for j, fruit in enumerate(good):
        if fruit[0].lower() in vowels:
            starts_with_vowel.append((i, j))

print(starts_with_vowel)