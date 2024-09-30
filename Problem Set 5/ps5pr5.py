# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:53:01 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""
def index(elem, seq):
    '''returns the index of the first occurrence of elem in seq.'''
    if seq == '' or seq == []:
        return -1
    elif seq[0] == elem:
            return 0
    else:
        rest = index(elem, seq[1:])
        if rest == -1:
            return rest
        else:
            return rest + 1
 
def rem_first(elem, seq):
    '''removes first occurences of elem from the list.'''
    if seq == '':
        return ''
    elif seq[0] == elem:
        return seq[1:]
    else:
        rest = rem_first(elem, seq[1:])
        return seq[0] + rest      

def jscore(s1, s2):
    '''returns the Jotto score of s1 compared with s2 – i.e., the number of 
    characters in s1 that are shared by s2.'''
    count = 0
    if s1 == '' or s2 == '':
        return 0
    else:
        if s1[0] in s2:
            return count + 1 + jscore(s1[1:], rem_first(s1[0], s2))
        else:
            return count + jscore(s1[1:], rem_first(s1[0], s2))

def rem_upto(c, s):
    '''Returns a version of s in which everything up to and including
    the first occurence of the character c is removed. If c is not in s, 
    returns s.'''
    if s == '':
        return ''
    elif c not in s:
        return s
    elif s[0] == c:
        return s[1:]
    else: 
        rest = rem_upto(c, s[1:])
        return rest

def lcs(s1, s2):
    '''returns the longest common subsequence (LCS) that s1 and s2 share.'''
    if s1 == '' or s2 == '':
        return ''
    else:
        if s1[0] == s2[0]:
            return s1[0] + lcs(s1[1:], s2[1:])
        else:
            result1 = lcs(s1[1:], rem_upto(s1[0], s2))
            result2 = lcs(rem_upto(s2[0], s1), s2[1:])
            if len(result1) > len(result2):
                return result1
            else:
                return result2

if __name__ == '__main__':
    
    #index test cases.
    print(index(5, [4, 10, 5, 3, 7, 5]))
    print(index(3, [2, 4, 6]))
    print(index('hi', ['well', 'hi', 'there']))
    print(index('a', ''))
    print(index(42, []))
    
    #jscore test cases.
    print(jscore('recursion', ''))
    print(jscore('recursion', 'excursion'))
    print(jscore('always', 'walking'))
    
    print(rem_upto('e', 'yellow submarine'))
    
    #lcs test cases.
    print(lcs('human', 'chimp'))
    print(lcs('gattaca', 'tacgaacta'))
    print(lcs('abcdefgh', 'efghabcd'))
    print(lcs('yellow submarine', 'hello, goodbye'))