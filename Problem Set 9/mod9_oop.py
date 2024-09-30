# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:59:21 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: Problem set 9 examples.
"""

class Point:
    '''a blueprint for objects that represent a point on the 
    cartesian plane.'''
    def __init__(self, init_x, init_y):
        '''the Point constructor'''
        #initialize the data members
        self.x = init_x
        self.y = init_y
        
    #move method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    #__repr__ method
    def __repr__(self):
        return f"Point(({self.x}, {self.y}))"
    
    #__eq__ method
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
        
#client code for Point.
#Construct two Point objects.
p1 = Point(100, 50)
p2 = Point(75, 350)

#Print position of each. (Uses __repr__).
print(f'p1: ({p1.x}, {p1.y})')
print(f'p2: ({p2.x}, {p2.y})')

#Move both Points. (Uses __repr__).
p1.x += 50 
p1.y += 10
p2.x += 5
p2.y += 30

#Print new position of each.
print(f'p1: ({p1.x}, {p1.y})')
print(f'p2: ({p2.x}, {p2.y})')

#Using the move method and printing p1 to show the change.
p1.move(25, 100)
print(f'p1: ({p1.x}, {p1.y})')

if __name__ == '__main__':

    #Type method.
    print(type(111))   #prints 'int' because 111 is an integer
    print(type(3.14159))   #prints 'float' because 3.14159 is a float.
    print(type('hello!'))   #prints 'str' because 'hello!' is a string.
    
    #Trying to print out an object without __repr__.
    print(p2)
    
    #using the __eq__ method.
    p3 = Point(40, 75)
    p4 = Point(40, 75)
    print(p3 == p4)

