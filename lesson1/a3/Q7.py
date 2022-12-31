# Write a code that receives the year as input and prints whether the year is a leap year or not.
# To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not. 2020, 2024 and 2028 are all leap years.

year = int(input("Please enter a year: "))
if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
