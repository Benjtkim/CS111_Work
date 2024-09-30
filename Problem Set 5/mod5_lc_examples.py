# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:53:52 2024

@author: benjt
"""

def mylen(seq):
   '''Find the length of a sequence 
      using a list comprehension.'''

   lc = [1 for x in seq]
   return sum(lc)

def num_vowels(s):
   '''Find the number of vowels in a string 
      using a list comprehension.'''

   lc = [1 for c in s if c in 'aeiou']
   return sum(lc)

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

def best_word(words):
    '''Returns the word from the input list of words with the best Scrabble
    Score.'''
    scored_words = [[scrabble_score(w), w] for w in words]
    bestpair = max(scored_words)
    return bestpair[1]

if __name__ == '__main__':
    
    #mylen test cases.
    print(mylen([1,2,3,4,5]))
    print(mylen([3,4,10]))
    print(mylen([]))
    
    #num_vowels test cases.
    print(num_vowels('hello'))
    print(num_vowels('absolutely'))
    
    #best_word test case.
    print(best_word(['aliens', 'zap', 'hazy', 'code']))
    
