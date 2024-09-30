# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:50:40 2024

@author: benjt
"""

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

def power(b, p):
    if p == 1:
        return b
    return b * power(b, p - 1)

def mylen(s):
    if s == '':
        return 0
    else:
        len_rest = mylen(s[1:])
        return len_rest + 1

def mymax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_in_rest = mymax(lst[1:])
        if lst[0] > max_in_rest:
            return lst[0]
        else:
            return max_in_rest

def replace(s, old, new):
    if old not in s:
        return s
    else:
        rest = replace(s[1:], old, new)
        if s[0] == old:
            return new + rest
        else:
            return s[0] + rest

def remove_vowels(s):
    if s == '':
        return ''
    else:
        rest = remove_vowels(s[1:])
        if s[0] in 'aeiou':
            return rest
        else:
            return s[0] + rest

def powers_of(x, n):
    if n == 0:
        return [1]
    else:
        rest = powers_of(x, n - 1)
        return rest + [x ** n]
    
if __name__ == '__main__':
    
    # fac test case.
    print(fac(5))
    
    #power test case.
    print(power(2, 5))
    
    #mylen test case.
    print(mylen('super'))
    
    #mymax test case:
    print(mymax([5, 6, 10, 1, 3]))
    print(mymax([1]))
    print(mymax([10, 2, 3, 4]))
    
    #replace test case:
    print(replace('boston', 'o', 'e'))
    
    #remove_vowes test case:
    print(remove_vowels('after'))
    
    #powers_of test case:
    print(powers_of(2,5))