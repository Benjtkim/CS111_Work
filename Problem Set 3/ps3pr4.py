# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 08:28:12 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def letter_score(letter):
    '''takes a lowercase letter and returns the value of that letter as a 
    scrabble tile.'''
    if letter.isalpha() == False or letter.islower() == False or len(letter) != 1:
        return 0
    else:
        if letter in ['e','a','i','o','n','r','t','l','s','u']:
            return 1
        elif letter in ['d','g']:
            return 2
        elif letter in ['b','c','m','p']:
            return 3
        elif letter in ['f','h','v','w','y']:
            return 4
        elif letter in ['j','x']:
            return 8
        elif letter in ['q','z']:
            return 10
        else:
            return 5

def scrabble_score(word):
    '''takes a string (word) containing only lowercase letters, and uses 
    recursion to return the scrabble score of that string.'''
    if word == '':
        return 0
    else:
        rest = scrabble_score(word[1:])
        return letter_score(word[0]) + rest

def add(vals1, vals2):
    '''takes two lists of 0 or more numbers, vals1 and vals2, and uses 
    recursion to return a new list in which each element is the sum of the 
    corresponding elemnts of vals1 and vals2.'''
    if vals1 == []:
        return []
    else:
        rest = add(vals1[:-1], vals2[:-1])
        return rest + [vals1[-1] + vals2[-1]]   

def weave(s1,s2):
    '''takes two strings, s1 and s2, and uses recursion to 
    return a new string that is formed by “weaving” together the characters in 
    s1 and s2.'''
    if len(s1) > len(s2) and s2 == '':
        return s1
    elif len(s2) > len(s1) and s1 == '':
        return s2
    elif len(s1) == len(s2) and s1 == '':
        return ''
    else:
        rest = weave(s1[1:], s2[1:])
        return s1[0] + s2[0] + rest

if __name__ == '__main__':
    
    #letter_score test cases.
    print(letter_score('w'))
    print(letter_score('q'))
    print(letter_score('%'))
    print(letter_score('A'))
    print(letter_score('ww'))
    
    #scrabble_score test cases.
    print(scrabble_score('python'))
    print(scrabble_score('a'))
    print(scrabble_score('quetzal'))
    
    #add test cases.
    print(add([1, 2, 3], [3, 5, 8]))
    print(add([2, 3, 4, 5], [-3, -2, -1, 0]))
    print(add([], []))
    
    #weave test cases.
    print(weave('aaaaaa', 'bb')) 
    print(weave('abcde', 'VWXYZ'))
    print(weave('aaaa', ''))
    print(weave('', 'bbbb'))
    print(weave('', ''))
    