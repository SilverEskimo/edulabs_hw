symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_int(roman_string: str)  -> int:
    res_int = 0
    skip_next_iteration = False
    for i, char in enumerate(roman_string):
        if i < len(roman_string) - 1:
            if symbols[roman_string[i]] < symbols[roman_string[i + 1]]:
                res_int += symbols[roman_string[i + 1]] - symbols[roman_string[i]]
                skip_next_iteration = True
            elif not skip_next_iteration:
                res_int += symbols[char]
                skip_next_iteration = False
            else:
                skip_next_iteration = False
        else:
            if not skip_next_iteration:
                res_int += symbols[char]
    return res_int


if __name__ == '__main__':
    user_input = input("Please enter a number in roman symbols: ").strip()
    print(roman_to_int(user_input))
