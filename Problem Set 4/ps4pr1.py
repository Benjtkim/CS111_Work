# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:34:05 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def dec_to_bin(n):
    ''' takes a non-negative integer (n) and converts it from decimal to 
    binary.'''
    if n == 0:
        return str(0)
    elif n == 1:
        return str(1)
    else:
        if n % 2 != 0:
            return dec_to_bin(n // 2) + str(1)
        else:
            return dec_to_bin(n // 2) + str(0)

def bin_to_dec(b):
    '''takes a string (b) that represents a binary number and converts the 
    number from binary to decimal.'''
    if b == '0':
        return 0
    elif b == '1':
        return 1
    else:
        left_shift = bin_to_dec(b[:-1])
        if b[-1] == '1':
            return 2 * left_shift + 1
        else:
            return 2 * left_shift

if __name__ == '__main__':
    
    #dec_to_bin test cases.
    print(dec_to_bin(5))
    print(dec_to_bin(12))
    print(dec_to_bin(111))
    print(dec_to_bin(128))
    
    #bin_to_dec test cases.
    print(bin_to_dec('0'))
    print(bin_to_dec('1'))
    print(bin_to_dec('00011010'))
    print(bin_to_dec('1111111'))
    