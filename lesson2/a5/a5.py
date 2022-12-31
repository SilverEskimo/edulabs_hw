# # You have the following list
l = [
        ['Paris', 'London', 'New York'],
        [45, True, 5.5, 'hello'],
        -3,
        [
            5, ['#', '$', '%', '^', [10, 20, 30, 40]]
        ],
        [
            ['a'], ['b'], 'c', [['d']]
        ]
]


# 1. -3 (int) - done
# 2. 5.5 (float) - done
# 3. ['New York', 'London', 'Paris'] - done
# 4. [[45, True, 5.5, 'hello'], -3] - done
# 5. '^'(str) - done
# 6. 'a' (str) - done
# 7. ['b'](list) - done
# 8. d' (str) - done
# 9. [20, 40](list) - done
# 10. ['^', '#'] (list) - done

#1
print(l[2])
#2
print(l[1][2])
#3
print([l[0][2], l[0][1], l[0][0]])
#4
print([l[1], l[2]])
#5
print(l[3][1][3])
#6
print(l[4][0][0])
#7
print(l[4][1])
#8
print(l[4][-1][0][0])
#9
print(l[3][1][-1][1::2])
#10
print(l[3][1][3::-3])
