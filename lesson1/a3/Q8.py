#After you implement 6 and 7, merge your solutions and write a program that receives
#3 numbers that represent a date (day, month, year),and prints out the season name of the date (winter, summer, autumn, winter)
#and the amount of days in the month, taking leap years into account!


day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))
year = int(input ("Please enter the year: "))

leap_year = False

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True

if 1 <= month <= 2 or month == 12:
    if month != 2:
        print("Winter, 31 days")
    elif not leap_year:
        print("Winter, 28 days")
    else:
        print("Winter, 29 days")
elif 3 <= month <= 5:
    if month != 4:
        print("Spring, 31 days")
    else:
        print("Spring, 30 days")
elif 6 <= month <= 8:
    if month != 6:
        print("Summer, 31 days")
    else:
        print("Summer, 30 days")
else:
    if month != 10:
        print("Autumn, 30 days")
    else:
        print("Autumn, 31 days")


