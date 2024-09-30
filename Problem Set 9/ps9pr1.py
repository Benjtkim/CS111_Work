#
# ps9pr1.py (Problem Set 9, Problem 1)
#
#Date: 8/2/24
#Name: Benjamin Kim
#email: benjt@bu.edu
#Description: A class to represent calendar dates
#

class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """

        # the f-string enables substitutions inside a string
        # expressions inside { } are evaluated at runtime
        s =  f'{self.month:02d}/{self.day:02d}/{self.year:04d}'
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
#### Put your code below. ####
    def advance_one(self):
        '''changes the called object so that it represents one calendar 
        day after the date that it originally represented.
        '''
        #days_in_month list. Index 0 is 0 so the rest of the indices line
        #up with the numerical dates.
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        #Df the day is the highest allowable day for that month and it's not 
        #December or Feburary, increase the month by 1 and set the day to 1.
        if (days_in_month[self.month] == self.day and self.month != 12 
            and self.month != 2):
            self.month += 1
            self.day = 1
        
        #If it's Feburary, not a leap year, and the 28th, increase the month 
        #by 1 and set the day to the 1st.
        elif (self.month == 2 and Date.is_leap_year(self) == False 
              and self.day == 28):
            self.month += 1
            self.day = 1
            
        #If it's December and the day is the 31st, increase the year by 1, set
        #the month to January, and set the day to the 1st.
        elif self.month == 12 and self.day == 31:
            self.year += 1
            self.month = 1
            self.day = 1
            
        #If it's a leap year, and Feburary, and the 2nd, set the month to 
        #March and the day to the 1st.
        elif (Date.is_leap_year(self) == True and self.month == 2 
              and self.day == 29):
            self.month += 1
            self.day = 1
        
        #In all other cases, simply increase the day by 1.
        else:
            self.day += 1
            
    def advance_n(self,n):
        '''changes the calling object so that it represents n calendar 
        days after the date it originally represented.
        '''
        #In this method, we're simply calling advance_one n times.
        print(self)
        for i in range(n):
            Date.advance_one(self)
            print(self)

    def __eq__(self, other):
        '''returns True if the called object (self) and the argument 
        (other) represent the same calendar date and false otherwise.
        '''
        #If all of the numbers match, the method returns true. Otherwise, 
        #false.
        return (self.day == other.day and self.month == other.month and 
                self.year == other.year)
    
    def is_before(self, other):
        '''returns True if the called object represents a calendar date 
        that occurs before the calendar date that is represented by other.
        '''
        #If the other date's year is greater, return true.
        if other.year > self.year:
            return True
        #Failing the first if statement, if the other month is greater, 
        #return true.
        elif other.year == self.year and other.month > self.month:
            return True
        #Failing the above two if statements, if the other day is greater,
        #return true.
        elif (other.year == self.year and other.month == self.month 
              and other.day > self.day):
            return True
        #Failing every if statement, return false.
        else:
            return False
    
    def is_after(self, other):
        '''returns True if the calling object represents a calendar date 
        that occurs after the calendar date that is represented by other.
        '''
        #If the other date comes before the calling object date, then 
        #the calling object date must come after the other date.
        if Date.is_before(other, self) == True:
            return True
        else: 
            return False
        
    def days_between(self, other):
        '''returns an integer that represents the number of days between 
        self and other.
        '''
        new_date1 = self.copy()
        new_date2 = other.copy()
        #Accumulator variable for the while loops.
        count = 0
        #If the two dates are equal, return 0
        if new_date1 == new_date2:
            return 0
        
        #If the calling object date is before the other date, increase the
        #calling object date until it's equal to the other date, recording
        #each increase to count.
        elif Date.is_before(new_date1, new_date2) == True:
            while new_date1 != new_date2:
                Date.advance_one(new_date1)
                count += 1
            
            #Return that recording but multiplied by -1.
            return count * -1
        
        #if the calling object date is after the other date, increase the
        #other date until it's equal to the calling object date, recording
        #each increase to count.
        elif Date.is_after(new_date1, new_date2) == True:
            while new_date2 != new_date1:
                Date.advance_one(new_date2)
                count += 1
            return count
    
    def day_name(self):
        '''returns a string that indicates the name of the day of the week 
        of the Date object that calls it.
        '''
        #day_names helper list.
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        #Set the reference date equal to June, 10, 2024 because we know it's
        #a Monday.
        reference_date = Date(6, 10, 2024)
        
        #Calculate how many days we will have to change by taking the modulus 
        #7 of the number of days in between our reference date and our 
        #calling ojbect date.
        day_change = Date.days_between(self, reference_date) % 7
        
        #if day_change is positive and less than 7, simply return names
        #index day_change.
        if day_change > 0 and day_change < 7:
            return day_names[day_change]
        
        #if day_change is positive and greater than 7, return names
        #index day_change - 7.
        elif day_change > 0 and day_change > 7:
            return day_names[day_change - 7]
        
        #if day_change is negative and greater than -7, return names
        #index day_change * -1.
        elif day_change < 0 and day_change > -7:
            return day_names[day_change * -1]
        
        #if day_change is negative and less than -7, return names
        #index (day_change + 7) * -1.
        elif day_change < 0 and day_change < -7:
            return day_names[(day_change + 7) * -1]
        
        else:
            return day_names[0]
            
        
if __name__ == '__main__':
    
    d1 = Date(4, 15, 2024)
    
    #Examples of using the __repr__ method.
    print(d1)
    print(d1.month)
    
    #Check if d1 is in a leap year.
    print(d1.is_leap_year())
    
    d2 = Date(4, 15, 2019)
    
    #Check if d2 is in a leap year.
    print(d2.is_leap_year())
    
    d3 = Date(1, 1, 2024)
    d4 = d3
    d5 = d3.copy()
    
    #Determine the memory addresses to which the variables refer.
    print(id(d3))
    #d2 is a reference to the same Date that d1 references.
    print(id(d4))
    #d3 is a reference to a different Date in memory.
    print(id(d5))   
    #Shallow copy -- d1 and d2 have the same memory address.
    print(d3 == d4)   
    #This is a deep copy -- d1 and d3 have different memory addresses. 
    #Printed false before implementing __eq__.
    print(d3 == d5)  
    
    #advance.one test cases.
    d6 = Date(8, 1, 2024)
    d6.advance_one()
    print(d6)
    d7 = Date(8, 31, 2024)
    d7.advance_one()
    print(d7)
    d8 = Date(12, 31, 2024)
    d8.advance_one()
    print(d8)    
    d9 = Date(2, 28, 2023)
    d9.advance_one()
    print(d9)
    d10 = Date(2, 29, 2024)
    d10.advance_one()
    print(d10)
    print('--------')
    
    #advance_n test cases.
    d11 = Date(8, 1, 2024)
    d11.advance_n(3)
    print(d11)
    d12 = Date(8, 1, 2024)
    d12.advance_n(0)
    print(d12)
    d13 = Date(8, 1, 2024)
    d13.advance_n(300)
    print(d13)
    print('--------')
    
    #is_before test cases.
    ny = Date(1, 1, 2024)
    d14 = Date(11, 15, 2023)
    d15 = Date(3, 24, 2023)
    tg = Date(11, 23, 2023)
    print(ny.is_before(d14))
    print(d14.is_before(ny))
    print(d14.is_before(d15))
    print(d15.is_before(d14))
    print(d14.is_before(tg))
    print(tg.is_before(d14))
    print(tg.is_before(tg))
    print('--------')
    
    #is_after test cases.
    ny = Date(1, 1, 2024)
    d16 = Date(11, 15, 2023)
    d17 = Date(3, 24, 2023)
    tg = Date(11, 23, 2023)
    print(ny.is_after(d16))
    print(d16.is_after(ny))
    print(d16.is_after(d17))
    print(d17.is_after(d16))
    print(d16.is_after(tg))
    print(tg.is_after(d16))
    print(tg.is_after(tg))
    print('--------')
    
    #days_between test case.
    d18 = Date(12, 1, 2023)
    d19 = Date(3, 15, 2024)
    print(d19.days_between(d18))
    print(d18.days_between(d19))
    
    #day_name test cases.
    d20 = Date(6, 11, 2024)
    print(d20.day_name())
    d21 = Date(6, 17, 2024)
    print(d21.day_name())
    print(Date(7, 1, 2024).day_name())
    print(Date(7, 4, 1776).day_name())   
