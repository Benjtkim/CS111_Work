# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:05:14 2024

Name: Benjamin Kim
email: benjt@bu.edu
Decription: This file contains 3 functions that use definite loops.
"""

def print_squares(values):
    '''Takes a list of numbers (values) and prints out the square of 
    each value.'''
    #For loop that iterates through each value and prints out that value to 
    #the power of 2.
    for value in values:
        print(value**2)

def print_multiples(n, m):
    '''Returns a list of the first n multiples of the integer m.'''
    #For loop that iterates through 0 to m-1 and prints each number multiplied
    #by n.
    for i in range(m):
        print(i*n)

def num_vowels(s):
    '''Returns the number of vowels that are in the string s.'''
    #Accumulator variable that allows us to keep track of the # of vowels. 
    result = 0
    
    #For each character in s, if the character is a vowel add 1 to result.
    for ch in s:
        if ch in 'aeiou':
            result += 1
            
    #Else, add nothing.
        else: 
            result += 0
            
    return result

if __name__ == '__main__':
    
    #print_squares test cases.
    print_squares([6,7,8])
    print_squares([1.2, 2.5])
    print_squares([1,2,3])
    
    #print_multiples test cases.
    print_multiples(2, 10)
    print_multiples(12, 5)
    print_multiples(4, 8)
    
    #num_vowels test cases.
    print(num_vowels('chocolate'))
    print(num_vowels('chocolate therapy ice cream'))
    
