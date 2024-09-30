# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 08:18:03 2024

@author: benjt
"""

def my_min(a,b):
    """This function takes 2 parameters and returns the minimum of those two."""
    if a > b:
        return b
    return a

def find_min(a, b, c):
    """This function takes 3 parameters and returns the minimum of those three."""
    if a < b and a < c:
        return a
    elif b < c:
        return b
    return c

def longer_len(s1, s2):
    """This function takes two string values (s1) and (s2), and returns the length of the longer string."""
    if len(s1) > len(s2):
        return len(s1)
    return len(s2)

def mirror(s):
    return s + s[-1:0:-1] + s[0]

def  is_mirror(s):
    """This function takes a string (s) and returns True if s is a mirrored string and False otherwise."""
    if len(s) % 2 != 0:
        return False
    elif s != mirror(s[0:len(s)//2]):
        return False
    return True

