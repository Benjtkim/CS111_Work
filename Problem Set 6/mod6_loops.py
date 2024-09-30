# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:52:49 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def elem_sum(lst):
    '''Element based loop.'''                 
    result = 0
    for x in lst:
        result += x
    return result

def index_sum(lst):  
    '''Index based loop.'''               
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result

def compute_multiples(m, n):
    '''Returns a list of the first n multiples of the integer m.'''
    result = []
    for i in range(n + 1):
        result.append(i*m)
    return result

def double_vowels(s):
    '''Returns a string such that each of the vowels in s is doubled.'''
    result = ''
    for i in range(len(s)):
        if s[i] in 'aeiou':
            result += 2 * s[i]
        else:
            result += s[i]
    return result

if __name__ == '__main__':
    
    #Element based loop test cases.
    print(elem_sum([1,2,3,4]))
    print(elem_sum([]))
    print(elem_sum([5,6,7,8]))
    
    #Index based loop test cases. Should return the same numbers as the test 
    #cases above.
    print(elem_sum([1,2,3,4]))
    print(elem_sum([]))
    print(elem_sum([5,6,7,8]))
    
    #compute_multipels test cases.
    print(compute_multiples(3,4))
    print(compute_multiples(10,5))
    print(compute_multiples(10,0))
    print(compute_multiples(0,2))
    
    #double_vowels test cases.
    print(double_vowels('coconut'))
    print(double_vowels('apple'))
    