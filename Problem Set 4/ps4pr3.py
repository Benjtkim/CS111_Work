# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 08:16:59 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def bitwise_and(b1, b2):
    '''takes two strings that represent binary numbers (b1 and b2), computes
    the bitwise AND of the two numbers, and returns the result in the form of 
    a string'''
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return '0' * len(b2)
    elif b2 == '':
        return '0' * len(b1)
    else:
        rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return rest + '0'
        elif b1[-1] == '0' and b2[-1] == '1':
            return rest + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return rest + '0'
        else:
            return rest + '1'
        
def add_bitwise(b1, b2):
    '''adds the two binary numbers b1 and b2.'''
    if b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return rest + '0'
        elif b1[-1] == '0'and b2[-1] == '1':
            return rest + '1'
        elif b1[-1] == '1' and b2 [-1] == '0':
            return rest + '1'
        else:
            return add_bitwise(rest, '1') + '0' 
        

if __name__ == '__main__':
    
    #bitwise_and test cases.
    print(bitwise_and('11010', '10011'))
    print(bitwise_and('1001111', '11011'))
    print(bitwise_and('', ''))
    print(bitwise_and('101', ''))
    print(bitwise_and('', '11010'))
    
    #add_bitwise test cases.
    print(add_bitwise('11100', '11110'))
    print(add_bitwise('10101', '10101'))
    print(add_bitwise('11', '1'))
    print(add_bitwise('11', ''))
    print(add_bitwise('', '101'))