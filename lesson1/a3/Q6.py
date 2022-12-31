# Write a code that receives 3 numbers that represent a date (day, month, year) and prints out the season name
# of the date (winter, summer, autumn, winter).
# In addition, print out the amount of days in the month (30, 31, or 28/29 for february).
# *No need to take leap years into account

#input example - 14 12 2022
#output example - Winter 31


day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))
year = int(input ("Please enter the year: "))

if 1 <= month <= 2 or month == 12:
    if month != 2:
        print("Winter, 31 days")
    else:
        print("Winter, 28 days")
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



