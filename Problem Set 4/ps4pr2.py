# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 08:02:10 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""
from ps4pr1 import *

def add(b1, b2):
    '''returns the binary sum of b1 and b2.'''
    new_sum = bin_to_dec(b1) + bin_to_dec(b2)
    return dec_to_bin(new_sum)

def increment(b):
    '''takes an 8-character string representation of a binary number (b) and 
    returns the next larger binary number as an 8-character string.'''
    if b == '11111111':
        return '00000000'
    else:
        target_number = bin_to_dec(b) + 1
        target_number_binary = dec_to_bin(target_number)
        if len(target_number_binary) < 8:
            return (8 - len(target_number_binary)) * '0' + target_number_binary
        else:
            return target_number_binary

if __name__ == '__main__':
    
    #add test cases.
    print(add('11', '1'))
    print(add('11100', '11110'))

    #increment test cases.
    print(increment('00000000'))
    print(increment('00000111'))
    print(increment('11111111'))
    print(increment('1111111'))