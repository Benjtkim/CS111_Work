# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:32:14 2024

@author: benjt
"""

def mystery(a,b):
    if a == 0 or a == 1:
        return b
    return a * b

print(mystery(0, 5))

def foo(x):
    if x > 10:
        print(x, "is greater than 10")
    else:
        print(x, "is less than or equal to 10")
	    
    if x % 2 == 1:
        print(x, "is odd")
    else:
        print(x, "is even")
	        
x = 33
foo(x)
y = 7
foo(y)
z = 12
foo(z)
z = 6
foo(z)

def example(x, var):
    if x in var:
        return True
    return False

print(example(3, [1,2,3,4,5]))
print(example('i', 'team'))