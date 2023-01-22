# Implement a function that receives a time in format hh:mm that represents the time when the lecture ends,
# and returns the amount of time left to the end of the lecture.
import datetime

if __name__ == '__main__':
    def time_left(end_time: str) -> str:
        hours, minutes = end_time.split(":")
        formatted_end_time = datetime.time(hour=int(hours), minute=int(minutes))
        current_time = datetime.datetime.now()
        ret_val = datetime.datetime.combine(datetime.datetime.today(), formatted_end_time) - \
            datetime.datetime.combine(datetime.datetime.today(), current_time.time())
        if str(ret_val)[0] == "-":
            return "The lecture has already ended"
        return str(ret_val)[:4] if str(ret_val)[1] == ":" else str(ret_val)[:5]

    print(time_left("23:59"))
