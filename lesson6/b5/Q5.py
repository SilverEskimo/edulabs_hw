# Create a function that receives my_cities and returns all the cities I’ve visited without duplications.
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


def return_cities(some_dict: dict) -> set:
    res_set = set()
    for year, visits in some_dict.items():
        if some_dict.get(year, {}):
            inner_dict = some_dict.get(year)
            for country, cities in inner_dict.items():
                for city in cities:
                    res_set.add(city)
    return res_set


print(return_cities(my_cities))
