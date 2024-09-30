# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 08:29:38 2024

@author: benjt
"""

def  is_valid_month(month):
    """This function returns True if the month is valid, and False otherwise."""
    if month > 0 and month < 13:
        return True
    return False

def is_leap_year(year):
    """This function returns True if the year is a leap year, and False otherwise."""
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def is_valid_day_in_month(month, day, year):
    """This function returns True if the day number is valid within the month, and False otherwise."""
    thirty_one_day_months = [1,3,5,7,8,10,12]
    thirty_day_months = [4,6,9,11]
    if is_valid_month(month) == False:
        return False
    
    if day < 32 and day > 0 and month in thirty_one_day_months:
        return True
    elif day < 31 and day > 0 and month in thirty_day_months:
        return True
    elif day < 29 and day > 0 and month == 2 and is_leap_year(year) == False:
        return True
    elif day < 30 and day > 0 and month == 2 and is_leap_year(year) == True:
        return True
    return False

def get_month_name(month):
    """This function takes an integer parameter (month) and returns the name of the month as a string."""
    month_names = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if month > 12 or month < 1:
        return "Can't return a name."
    else:
        return month_names[month - 1]
    
def is_valid_date(month, day, year):
    """This function  takes integer parameters for the month, day, and year, and returns True if it's a valid date 
    and False otherwise."""
    if is_valid_month(month) == False:
        print(str(month) + '/' + str(day) + '/' + str(year) + ' is not a valid date because ' + str(month) + ' is not a valid month.')
        return False
    elif is_valid_day_in_month(month, day, year) == False:
        print(str(month) + '/' + str(day) + '/' + str(year) + ' is not a valid date because day ' + str(day) + ' is not a valid day for ' + get_month_name(month) + ' ' + str(year) + '.')
        return False
    else:
        print(str(month) + '/' + str(day) + '/' + str(year) + ' is a valid date.')
        return True

