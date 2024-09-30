# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:40:56 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: More functions using definite loops. The new concept here is 
the range menthod used in conjunction with len.
"""

def double(s):
    '''Returns the string formed by doubling each character in the 
    string s.'''
    #Accumulator variable that will become the desired string.
    result = ''
    
    #Loop that iterates through each character in s, doubles it, and adds 
    #those characters to the accumulator variable.
    for ch in s:
        result += 2 * ch
    return result

def weave(s1, s2):
    '''returns a new string that is formed by “weaving” together the 
    characters in the strings s1 and s2.'''
    #Accumulator variable that will become the desired string.
    result = ''
    
    #Variable that stores the length of the shorter string.
    len_shorter = min(len(s1), len(s2))
    
    #If both strings are empty, return ''.
    if s1 == '' and s2 == '':
        return result
    
    #Loop that weaves together the new string.
    for i in range(len_shorter):
        result = result + s1[i] + s2[i]
    
    #If one string is shorter, appends the required characters to the new 
    #string.
    if len(s1) < len(s2):
        result = result + s2[len_shorter:-1] + s2[-1]
    elif len(s2) < len(s1):
        result = result + s1[len_shorter:-1] + s1[-1]
    
    return result

vals = [1,2,3,4,5,6]

def square_evens(values):
    '''modifies the list values so that all of its even elements are replaced 
    with their squares, but all of its odd elements are left unchanged.'''
    #First usage of an index-based loop to iterate through each value in the 
    #list values.
    for i in range(len(values)):
        
        #If that value is divisible by 2 (is even), replace that value at 
        #that index by its square.
        if values[i] % 2 == 0:
            values[i] = values[i] ** 2

def index(elem, seq):
    '''Returns the index of the first occurrence of elem in seq.'''
    #Another usage of an index-based loop to iterate through each element in 
    #the list seq.
    for i in range(len(seq)):
        
        #If that element is the desired one, return the index it's located at.
        if seq[i] == elem:
            return i
        
    #If the program runs through the entire list and does not find the desired
    #element, it returns -1.
    return -1


if __name__ == '__main__':
    
    #double test cases.
    print(double('hello'))
    print(double('python'))
    
    #weave test cases.
    print(weave('aaaaaa', 'bbbbbb'))
    print(weave('aaaaaa', 'bb') )
    print(weave('aaaa', 'bbbbbb'))
    print(weave('aaaa', '') )
    print(weave('', 'bbbb') )
    print(weave('', ''))
    
    #square_evens test cases.
    square_evens(vals)
    print(vals)
    
    #index test cases.
    print(index(5, [4, 10, 8, 5, 3, 5]))
    print(index('hi', ['well', 'hi', 'there']))
    print(index('b', 'banana'))
    print(index('i', 'team'))
    print(index(8, [4, 10, 5, 3]))