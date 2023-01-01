# How many words include “berry”?
# What are their indexes (2-number indices)?

goods = [
            ['apple', 'pear', 'peach', 'chery'],
            [
                'salak', 'mangustin', 'mango', 'durian', 'breadfruit',
                'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry'
            ]
]


count = 0
berry_indexes = []
for i, good in enumerate(goods):
    for j, fruit in enumerate(good):
        if 'berry' in fruit.lower():
            count += 1
            berry_indexes.append((i, j))

print(f"Berry is in the following words:\n{berry_indexes}")