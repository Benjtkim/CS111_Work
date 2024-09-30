#
# ps9pr3.py (Problem Set 9, Problem 3)
# Date: 8/2/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: More Date clients programs, this time with a dictionary.
#

# this import statement will allow your to use the Date class from ps9pr1.py
from ps9pr1 import Date

def nye_counts(start, end):
    '''counts how many times New Year’s Eve falls on each day of the week 
    between the years start and end, inclusive of both endpoints, and then 
    returns a dictionary containing those counts.'''
    d = {} # create an empty dictionary

    # add your code here
    #day_names helper list for later.
    day_names = ['Monday', 'Tuesday', 'Wednesday', 
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    #Loops through each year from start to end, including the end year.
    for year in range(start, end + 1):
        
        #The day we're seeking to find the day of the week for each year
        #is New Year's Eve. 
        nye_date = Date(12, 31, year)
        specific_day = Date.day_name(nye_date)
        
        #If the day of the week we found isn't in the dictionary, make it
        #a key and set its value to 1.
        if specific_day not in d:
            d[specific_day] = 1
            
        #Otherwise, increment its value.
        else:
            d[specific_day] += 1
    
    #For all the days of the week that aren't in the dictionary, make them
    #keys also and set their values to 0.
    for i in range(len(day_names)):
        if day_names[i] not in d:
            d[day_names[i]] = 0

    return d
    
if __name__ == '__main__':
    
    print(nye_counts(2014, 2016))