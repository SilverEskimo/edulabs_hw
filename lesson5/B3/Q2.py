# Implement a python program that receives a list of numbers that represent a triangle (each number in a list
# represents a side length of the triangle).
# Your program should print the perimeter and the area of the triangle. You should take into account the following:
# You cannot assume that the input is correct, so there is a need to check that the input is a list of exactly 3 numbers
# Not every 3 numbers make a triangle - In a proper triangle sum of each 2 sides should be bigger than the third side.


def is_valid_triangle(sides: list) -> bool:
    return sides[0] + sides[1] > sides[2] and \
           sides[0] + sides[1] > sides[1] and \
           sides[1] + sides[2] > sides[0]


def parse_input(user_inp: str) -> list[int] | None:
    split_list = user_inp.split(",")
    if len(split_list) != 3:
        return
    sides = []
    for side in split_list:
        if not side.isdigit() or side == '0':
            return
        sides.append(int(side))
    if is_valid_triangle(sides):
        return sides


def calc_perimeter(sides: list[int]) -> float:
    return sides[0] + sides[1] + sides[2]


def calc_area(sides: list[int]) -> float:
    s = calc_perimeter(sides) / 2
    area = (s * (s - sides[0])*(s - sides[1])*(s - sides[2]))**0.5
    return area


while True:
    user_input: str = input("Insert 3 sides of triangle separated by ,: ").strip()
    sides: list[int] = parse_input(user_input)
    if sides:
        break

print(f"The perimeter of the triangle is: "
      f"{calc_perimeter(sides)}")
print(f"The area of the triangle is: "
      f"{calc_area(sides)}")