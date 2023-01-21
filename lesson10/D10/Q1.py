# Implement a function that receives a float number that represents the amount of seconds as argument,
# and returns a formatted string that displays the amount of seconds in the format: hh:mm:ss.
# Hint: use datetime.timedelta for one-liner code 🙂
import datetime

if __name__ == '__main__':

    def return_formatted_hour(num_of_seconds: float) -> str:
        res = datetime.timedelta(seconds=num_of_seconds)
        return str(res)


    print(return_formatted_hour(60))