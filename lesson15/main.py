# write performance_log decorator that logs how long it took for a function to run
import time


def performance_log(some_func):
    def wrapping_func(*args, **kwargs):
        start = time.time()
        time.sleep(3)
        ret_val = some_func(*args, **kwargs)
        end = time.time()
        print(f"It took {end - start} seconds for {some_func.__name__} to run")
        return ret_val
    return wrapping_func


@performance_log
def power_of_num(num: int, pow_num: int):
    return num ** pow_num


if __name__ == '__main__':
    print("The res is:", power_of_num(16,16))