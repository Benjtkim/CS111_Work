# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:59:11 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: Module 11 examples.
"""

class Point:
    '''a blueprint for objects that represent a point on the 
    cartesian plane.'''
    
    def __init__(self, init_x, init_y):
        '''the Point constructor'''
        #initialize the data members.
        self.x = init_x
        self.y = init_y
    
    #__repr__ method.
    def __repr__(self):
        return f"Point(({self.x}, {self.y}))"
    
    #__eq__ method.
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    #move method.
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    #scale method.
    def scale(self, factor):
        self.x *= factor
        self.y *= factor
        
class Rectangle(Point):
    '''a blueprint for objectst that represent a rectangle on the cartesian
    plane.'''
    
    def __init__(self, x, y, width, height):
        '''the Rectangle constructor'''
        #Initialize the Point attributes by calling its constructor.
        super().__init__(x, y)
        
        #Initialize the Rectangle specific attributes.
        self.width = width
        self.height = height
        
    #__repr__method (subclass methods take priority).
    def __repr__(self):
        return f'Rectangle({self.width}x{self.height})'
    
    #Subclass scale method.
    def scale(self, amount):
        self.x *= amount
        self.y *= amount
        self.width *= amount
        self.height *= amount
        
    #New method only defined in the subclass.
    def area(self):
        return self.width * self.height 
    
if __name__ == '__main__':
        
    p1 = Point(100, 50)
        
    #__repr__ test case.
    print(p1)
    
    #__eq__ test case.
    p2 = Point(40, 75)
    p3 = Point(40, 75)
    print(p2 == p3)
    
    #move test case.
    p4 = Point(10, 10)
    p4.move(40, 40)
    print(p4)
    
    #scale test case.
    p5 = Point(5, 10)
    p5.scale(10)
    print(p5)
    
    r1 = Rectangle(40, 20, 10, 20)
    
    #__repr__ test case for rectangle.
    print(r1)
    
    #__eq__ test case for rectangle.
    r2 = Rectangle(10, 20, 40, 75)
    r3 = Rectangle(10, 20, 40, 75)
    print(r2 == r3)
    
    #move test case for rectangle.
    r4 = Rectangle(10, 10, 10, 10)
    r4.move(40, 40)
    print(r4)
    
    #scale test case for rectangle.
    r5 = Rectangle(10, 20, 10, 50)
    r5.scale(10)
    print(r5)
    
    #Area method test case.
    r6 = Rectangle(10, 20, 10, 50)
    print(r6.area())
    
    s = 'springtime'
    print(s[len(s) - 1:0:-1])