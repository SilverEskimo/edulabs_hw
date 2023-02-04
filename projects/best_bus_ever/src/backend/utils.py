import datetime
from best_bus_ever.src.backend.scheduled_ride import ScheduledRide


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def convert_rides(rides: list):
        converted_rides = []
        for ride in rides:
            converted_rides.append(ScheduledRide(datetime.datetime.strptime(ride, "%d/%m/%Y %H:%M")))
        return converted_rides
