"""
Checking for a leap year 2024--> yes
Leap day occurs in each year that is a multiple of 4,
except for years evenly divisible by 100 not by 400.

The year is multiple of 400
The year is a multiple of 4 and not a multiple of 100
"""
from operator import truediv


def check_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

year=2025
result = check_leap_year(year)
print(result)


