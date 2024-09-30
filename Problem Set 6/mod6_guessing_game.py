# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:46:49 2024

Name: Benjamin Kim
email: benjt@bu.edu
"""

import random

#pick a random number
secret = random.randint(1, 10)
print('Pick a number between 1 and 10.')
guess = int(input('Input your guess here: '))

#A loop that allows the user to keep guessing if they get the number wrong.
while guess != secret:
    print("Wrong!")
    
    if guess < secret:
        print("Too low!")
        guess = int(input('Input your guess here: '))
    else:
        print("Too high!")
        guess = int(input('Input your guess here: '))
        
if guess == secret:
    print("You guessed the correct number! Horray!")

