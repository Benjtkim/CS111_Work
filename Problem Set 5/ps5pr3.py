# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:31:59 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

def cube_all_lc(values):
    '''Uses list comprehension to take a list of numbers (values) and return 
    a list containing the numbers in values cubed.'''
    return [x**3 for x in values]

def cube_all_rec(values):
    '''Uses recursion to take a list of numbers (values) and return 
    a list containing the numbers in values cubed.'''
    if values == []:
        return []
    else:
        rest = cube_all_rec(values[1:])
        return [values[0]**3] + rest
        
def num_larger(threshold, values):
    '''Uses recursion to take a list of numbers (values) and return the number 
    of elements of values that are larger than threshold.'''
    if values == []:
        return 0
    else:
        rest = num_larger(threshold, values[1:])
        if values[0] > threshold:
            return rest + 1
        else:
            return rest 
        
def num_vowels(s):
   '''Find the number of vowels in a string 
      using a list comprehension.'''

   lc = [1 for c in s if c in 'aeiou']
   return sum(lc)

def most_consonants(words):
    '''Takes a list of strings (words) and returns the word with the most 
    consonants.'''
    if words == []:
        return ''
    else:
        rest = most_consonants(words[1:])
        if (len(words[0]) - num_vowels(words[0])) > (len(rest) - num_vowels(rest)):
            return words[0]
        else:
            return rest
        

if __name__ == '__main__':
    
    #cube_all_lc test cases.
    print(cube_all_lc([-2, 5, 4, -3]))
    print(cube_all_lc([1, 2, 3]))
    
    #cube_all_rec test cases.
    print(cube_all_rec([-2, 5, 4, -3]))
    print(cube_all_rec([1, 2, 3]))
    
    #num_larger test cases.
    print(num_larger(5, [1, 7, 3, 5, 10]))
    print(num_larger(2, [1, 7, 3, 5, 10]))
    
    #most_consonants test cases.
    print(most_consonants(['python', 'is', 'such', 'fun']))
    print(most_consonants(['oooooooh', 'i', 'see', 'now']))
    