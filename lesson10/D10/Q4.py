# Write a function that receives a date in format dd-mm-yy, and returns a date of the upcoming Friday as
# string in format: dd-mm-yyyy
import datetime

if __name__ == '__main__':
    def return_next_friday(date: str) -> str:
        date_time = datetime.datetime.strptime(date, "%d-%m-%Y")
        return (date_time + datetime.timedelta(4 - date_time.weekday())).strftime("%d-%m-%Y")

    print(return_next_friday("18-01-2023"))
