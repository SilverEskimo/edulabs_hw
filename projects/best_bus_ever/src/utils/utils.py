import datetime
from best_bus_ever.src.utils.exceptions import *


class Utils:
    @staticmethod
    def convert_ride_times(ride_times: tuple):
        converted_times = []
        for time in ride_times:
            try:
                converted_times.append(datetime.datetime.strptime(time, "%H:%M").time())
            except ValueError:
                raise WrongTimeFormat(f"Error: Wrong time format {time}.")
        return converted_times
    @staticmethod
    def convert_delay_date(delay_date: str):
        try:
            return datetime.datetime.strptime(delay_date, "%d/%m/%Y")
        except ValueError:
            raise WrongDateFomat(f"Error: wrong date format, should be dd/mm/yyyy")