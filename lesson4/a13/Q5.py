# Get 10 dates from the user. The date is in the following format: dd.mm.yyyy (no need to check.
# After you get all the 10 dates, print the amount of dates in winter, autumn, sprint, summer, and print the dates themselves.
# The output should look something like:
#
# You entered 2 dates in winter:
# 11.12.2013
# 05.01.1999
#
# You entered 8 dates in summer:
# 16.08.2012
# 05.07.1999

dates = []
seasons = (["summer"], ["winter"], ["autumn"], ["spring"])

for i in range(10):
    dates.append(input(f"Please enter the {i + 1} date: "))

for date in dates:
    _, m, _ = date.split(".")
    month = int(m)
    if month in (12, 1, 2):
        for season in seasons:
            if season[0] == "winter":
                season.append(date)
    elif month in (3, 4, 5):
        for season in seasons:
            if season[0] == "spring":
                season.append(date)
    elif month in (6, 7, 8):
        for season in seasons:
            if season[0] == "summer":
                season.append(date)
    else:
        for season in seasons:
            if season[0] == "autumn":
                season.append(date)

for season in seasons:
    print(f'You have entered {len(season) - 1} dates in {season[0]}:')
    for date in season[1:]:
        print(date)
