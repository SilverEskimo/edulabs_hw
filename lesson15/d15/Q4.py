# Implement a decorator @numeric_in_range that receives as parameters allowed range for numeric arguments
# (2 numbers - min and max) and validates that all the numerical arguments passed to the decorated function
# are in the range specified. If the validation fails, your decorator should raise an InvalidArgument exception.


class InvalidArgument(Exception):
    def __init__(self):
        super().__init__("The provided values are not in the allowed range")


def numeric_in_range(minimum: int, maximum: int):
    def wrapper(some_func):
        def wrapping_function(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if type(arg) in (float, int) and arg not in range(minimum, maximum):
                    raise InvalidArgument()
            return some_func(*args, **kwargs)
        return wrapping_function
    return wrapper


@numeric_in_range(10, 50)
def return_in_between(num1, num2, d=False, a=None):
    current_num = num1 + 1
    for num in range(num2 - num1 - 1):
        print(current_num, end=" ")
        current_num += 1


if __name__ == '__main__':
    try:
        return_in_between(11, 20)
    except InvalidArgument as e:
        print(e)