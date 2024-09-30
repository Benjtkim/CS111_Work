# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:48:38 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def double(s):
    '''This function takes an arbitrary string (s) and uses recursion to 
    construct and return the string formed by doubling each character in the 
    string.'''
    if s == '':
        return s
    return 2 * s[0] + double(s[1:])
        
def copy(s, n):
    '''This function takes a string (s) and an integer (n), and  uses 
    recursion to create and return a string in which n copies of s have been 
    concatenated together.'''
    if n <= 0 :
        return ''
    elif n == 1:
        return s
    return s + copy(s, n - 1)

def compare(list1, list2):
    '''This function takes two lists of numbers, list1 and list2, and uses 
    recursion to compute and return the number of values in list1 that are 
    smaller than their corresponding value in list2.'''
    if list1 == [] or list2 == []:
        return 0
    else:
        lst_rest = compare(list1[1:], list2[1:])
        if list1[0] < list2[0]:
            return 1 + lst_rest
        else:
            return lst_rest
    
if __name__ == '__main__':
    
    #double test cases.
    print(double('hello'))
    print(double('python'))
    
    #copy test cases.
    print(copy('da', 2))
    print(copy('Go BU!', 4))
    
    #compare test cases.
    print(compare([5, 3, 7, 9, 1], [2, 4, 7, 8, 3]))
    print(compare([4, 2, 3, 7], [1, 5]))