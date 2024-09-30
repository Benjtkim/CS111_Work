# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:51:15 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: Using the Date Class for client code.
"""

from ps9pr1 import Date

def get_age_on(birthday, other):
    '''accepts two Date objects as parameters: one to represent a 
    person’s birthday, and one to represent an arbitrary date. 
    The function then returns the person’s age on that date as an integer.
    '''
    #Calculate the number of years between the birthday and the other date
    #and return that value.
    return Date.days_between(other, birthday) // 365

def print_birthdays(filename):
    '''accepts a string filename as a parameter. The function then opens 
    the file that corresponds to that filename, reads through the file, 
    and prints some information derived from that file.
    '''
    #File handle. The bellow line of code opens the file and reads through 
    #it.
    file = open(filename, 'r')
    
    #For loop that iterates through each line in the file.
    for line in file:
        
        #Get rid of the newline.
        line = line[:-1]
        
        #Split each line so we have lists of the values we need.
        birthdays = line.split(',')
        
        #Get the person's birthday and save it to a variable to make the
        #code easier to read.
        date = Date(int(birthdays[1]), int(birthdays[2]), int(birthdays[3]))
        
        #Format the information in the desired way.
        print(birthdays[0], '(' + str(date) + ')', Date.day_name(date))
    
    #Close the file when we're done with it.
    file.close()

if __name__ == '__main__':
    
    #get_age_on test cases.
    birthday = Date(6, 29, 2004)
    d1 = Date(2, 10, 2024)
    print(get_age_on(birthday, d1))
    d2 = Date(11, 10, 2024)
    print(get_age_on(birthday, d2))
    
    #test to ensure print_birthdays works correctly.
    print_birthdays('birthdays.txt')