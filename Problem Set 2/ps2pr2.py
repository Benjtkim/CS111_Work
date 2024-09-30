# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:53:15 2024

@author: benjt
"""

def first_and_last(values):
    """This function takes a list (values) and returns a new list containing the first value of the original list 
    followed by the last."""
    first = values[0]
    last = values[-1]
    return [first, last]

def move_to_end(s, n):
    """This function takes a string value (s) and an integer (n), and  returns a new string in which the first n 
    characters of s have been moved to the end of the string."""
    if n > len(s):
        return s
    return s[n-len(s):] + s[0:n]

def truncate(s, max_length):
    """This function takes a string parameter (s) and an integer parameter (max_length), and returns the first 
    max_length characters of s."""
    if max_length > len(s):
        return s
    return s[0:max_length]

# Ask about the second example.
def triple_outsides(s):
    """This function takes a string (s), and returns a version of that string with the first and last characters 
    repeated 3 times, and the rest of the characters in the middle occuring only once each."""
    return s[0] + s[0] + s[0] + s[1:-1] + s[-1] + s[-1] + s[-1]
print(triple_outsides(" "))

def every_other(s):
    """This function takes a string (s) and returns a version of that string with every other character has been 
    skipped."""
    if len(s) % 2 == 0:
        return s[0:-1:2]
    return s[0:-1:2] + s[-1]

# Tell him you don't understand the question because the example is identical
# to move_to_end.
def rotate(s, n):
    """This function takes a string (s) and an integer (n), and returns a new string in which each character has 
    been moved n positions to the left."""
    if n > len(s):
        return s
    return s[n-len(s):] + s[0:n]

def mirror(s):
    """This function takes a string s and returns a mirrored version of s that is twice the length of the original 
    string."""
    return s + s[-1:0:-1] + s[0]

## Ask about using for loop.
def replace_end(values, new_end_vals):
    """This function takes a list (values) and another list (new_end_vals), and  returns a new list in which the 
    elements in new_end_vals have replaced the last n elements of the list values, where n is the length of 
    new_end_vals."""
    if len(new_end_vals) >= len(values):
        return new_end_vals
    else:
        for x in range(len(new_end_vals)):
            values[len(values) - len(new_end_vals) + x] = new_end_vals[x]
        return values

## Ask about using nested loops.
def repeat_elem(values, index, num_times):
    """This function takes a list (values), an integer (index), and a positive integer (num_times), and returns a 
    new list in which the element of values at position index has been repeated num_times times."""
    new_list = []
    for x in range(len(values)):
        if x != index:
            new_list.append(values[x])
        else:
            for x in range(num_times):
                new_list.append(values[index])
    return new_list


            


