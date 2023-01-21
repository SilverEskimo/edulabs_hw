# Implement a function that gets a string that represents datetime in the
# following format: "2021-12-08, Wed, 10:00" and returns the name of the weekday
# 3 days after the received date. For example, for the input provided, the output should be: Saturday.

import datetime

if __name__ == '__main__':
    def return_day_function(date: str) -> str:
        res = datetime.datetime.strptime(date, "%Y-%m-%d, %a, %H:%M") + datetime.timedelta(days=3)
        return res.strftime("%A")



    print(return_day_function("2021-12-08, Wed, 10:00"))