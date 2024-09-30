# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:34:49 2024

Name: Benjamin Kim
email: benjt@bu.edu
Decription: Creating and implementing a first-order Markov Model.
"""

import random

def create_markov_model(text):   
    '''Creates a dictionary of word transitions using the Markov Model.'''
    #Dictionary that we will store our key-value pairs into
    words_dict = {'$': []}
    
    #List of each word in text.
    words_list = text.split()
    
    #Index based loop to interate through all the words in words_list
    for i in range(len(words_list) - 1):
        #Using indices, current_word is the word we're currently on and 
        #next_word is the next word.
        current_word = words_list[i]
        next_word = words_list[i + 1]
        
        #Append the starting word to the empty list belonging to $, create
        #an empty list for the current_word key, and append next_word to 
        #said list.
        if i == 0:
            words_dict['$'].append(current_word)
            words_dict[words_list[i]] = []
            words_dict[words_list[i]].append(next_word)
            
        #If current_word ends in puncutation, set current_word to $,
        #and append next_word to its list.
        elif current_word.endswith('.' or '!' or '?') == True:
            current_word = '$'
            words_dict['$'].append(next_word)
        
        #If current_word is not in the dictionary, creates an empty list for 
        #it and appends the next_word into said list.
        elif current_word not in words_dict:
            words_dict[words_list[i]] = []
            words_dict[words_list[i]].append(next_word)
        
        #If current_word is in the dictionary, simply append next_word to 
        #the list current_word belongs to.
        else:
            words_dict[words_list[i]].append(next_word)
            
    return words_dict

def generate_markov_text(model, num_words):
    '''generates text using the Markov model.'''
    #Accumulator variable that will become the result of the Markov Model.
    result = ''
    
    #Current word begins with $
    current_word = '$'
    
    #for loop that runs num_words # of times.
    for i in range(num_words):
        
        #Using the dictionary created from create_markov_model, find 
        #the list belonging to current_word.
        following_words = model[current_word]
        
        #Pick a random word from said list to be the next_word
        next_word = random.choice(following_words)
        
        #Accumulate next_word to result along with a space.
        result = result + next_word + ' '
        
        #If next_word is a sentence ending word, current_word becomes $.
        if next_word.endswith('.' or '!' or '?') == True:
            current_word = '$'
        
        #Else, current_word becomes next_word.
        else:
            current_word = next_word
            
    return result

if __name__ == '__main__':
    #create_markov_model test case.
    text = 'A B A. A B C. B A C. C C C.'
    model = create_markov_model(text)
    print(model)
    
    #generate_markov_text test case.
    print(generate_markov_text(model, 20))
