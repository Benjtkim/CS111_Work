#
# File: ps1pr4.py - Problem Set 1, Problem 4
# Author name:
# Email:
# 
# Description: Functions with numeric inputs
#
# This is an individual-only problem that you must complete on your own.
#


#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
def cube(x):
    return x*x*x

def convert_to_inches(yards, feet):
    return yards * 36 + feet * 12

def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    return convert_to_inches(height_yds, height_ft) * convert_to_inches(width_yds, width_ft)

# TO DO: add test calls for your functions
# sample test call for function 0
print('opposite(-8) returns', opposite(-8))
print(cube(2))
print(convert_to_inches(4, 2))
print(area_sq_inches(2,0,1,2))
