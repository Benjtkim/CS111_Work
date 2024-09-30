# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:21:12 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""
def flipside(s):
    '''This function takes a string input (s) and returns a string whose 
    first half is s‘s second half and whose second half is s‘s first half.'''
    return s[(len(s)//2):] + s[:(len(s)//2)]

def adjust(s, length):
    '''This function takes a string (s) and an integer (length), and  returns 
    a string in which the value of s has been adjusted as necessary to produce 
    a string with the specified length.'''
    if len(s) < length:
        return " " * (length - len(s)) + s
    return s[:length]

if __name__ == '__main__':
    
    #flipside test cases.
    print(flipside('homework'))
    print(flipside('carpets'))

    #adjust test cases.
    print(adjust('alien', 6))
    print(adjust('compute', 5))