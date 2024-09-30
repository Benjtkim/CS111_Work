# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:07:23 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

#Left shift

#Should print 150 b/c 75 * 2^1 is 150 and adding a 0 to the right of a binary 
#number increases it twofold.
print(75 << 1) 

#Should print 20 because 5 * 2^2 is 20 and adding two 0s to the right of a 
#binary number increases it four-fold.
print(5 << 2)

#Should print 7 because dividing 15 by 2^1 and discarding the remainder 
#produces 7, and shifting all the bits in a binary number to the right removes
#the last bit, therefore reducing it twofold.
print(15 >> 1) 

#Should print 30 because dividing 120 by 2^2 produces 30, and shifting all the 
#bits in a binary number to the right two times removes the last two bits, 
#therefore reducing it four-fold.
print(120 >> 2)