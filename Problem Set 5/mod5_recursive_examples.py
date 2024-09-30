# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:54:07 2024

@author: benjt
"""

def rem_all(elem, lst):
    '''removes all occurences of elem from the list.'''
    if lst == []:
        return []
    else:
        rest = rem_all(elem, lst[1:])
        if lst[0] == elem:
            return rest
        else:
            return [lst[0]] + rest
        
def rem_first(elem, lst):
    '''removes first occurences of elem from the list.'''
    if lst == []:
        return []
    elif lst[0] == elem:
        return lst[1:]
    else:
        rest = rem_first(elem, lst[1:])
        return [lst[0]] + rest        

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

def is_subseq(s1, s2):
    '''Returns True if s1 is a subsequence of s2, and False otherwise.'''
    if s1 == '':
        return True
    elif s1[0] not in s2:
        return False
    else:
        s2_after = rem_upto(s1[0], s2)
        rest = is_subseq(s1[1:], s2_after)
        return rest

if __name__ == '__main__':
    
    #rem_all test cases.
    print(rem_all(10, [3,4,10,7,10]))
    print(rem_all(2, [1,2,2,5,16,20]))
    print(rem_all(0, [0,50]))
    
    #rem_first test cases.
    print(rem_first(10, [3,4,10,7,10]))
    print(rem_first(2, [1,2,2,5,16,20]))
    print(rem_first(0, [0,0,50]))
    
    #rem_upto test cases.
    print(rem_upto('s', 'you will always be a part of me.'))
    print(rem_upto('a', 'I work in an apple orchard.'))
    
    #is_subseq test cases.
    print(is_subseq('seem', 'you will always be a part of me.'))
    print(is_subseq('mag', 'magnificent'))
    print(is_subseq('nfi', 'magnificent'))