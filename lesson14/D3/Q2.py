def generator_batch(n: int, my_list: list):
    start = 0
    for i in range(int(len(my_list) / n)):
        res_list = my_list[start:start + n]
        start = start + n
        yield res_list
    if i != len(my_list):
        yield my_list[start:]


if __name__ == '__main__':
    print(list(generator_batch(4, list(range(1, 15)))))

