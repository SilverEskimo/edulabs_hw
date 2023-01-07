# Create a function that receives my_cities and returns dictionary arranged as follows:
# Keys = cities
# Values = all the dates when I was visiting the cities
# Example of output:
# my_cities_out = {'Berlin':[2008, 2010],....}

from pprint import pprint

my_cities = {
   2008: {
       'Germany':
           ['Berlin', 'Munich'],
       'France':
           ['Paris', 'Leon', 'Bordeaux']},
   2009: {
       'China':
           ['Hong Kong', 'Shanghai', 'Beijing'],
       'Japan':
           ['Nagoya', 'Toyokawa', 'Yatomi'],
       'Mexico':
           ['Tijuana', 'Ecatepec']},
   2010: {
       'Germany':
           ['Berlin', 'Dusseldorf'],
       'France':
           ['Paris', 'Nice', 'Bordeaux'],
       'Japan':
           ['Tokyo', 'Toyokawa', 'Yatomi']}
}


def return_cities_set(some_dict: dict) -> set:
    res_set = set()
    for year, visits in some_dict.items():
        if some_dict.get(year, {}):
            inner_dict = some_dict.get(year)
            for country, cities in inner_dict.items():
                for city in cities:
                    res_set.add(city)
    return res_set


def return_cities_with_years(some_dict: dict) -> dict:
    res_dict = {}
    cities_set = return_cities_set(some_dict)
    for city in cities_set:
        res_dict[city] = []
        for year, visits in some_dict.items():
            for country in some_dict.get(year):
                if city in some_dict.get(year).get(country):
                    res_dict[city].append(year)
    return res_dict


pprint(return_cities_with_years(my_cities))