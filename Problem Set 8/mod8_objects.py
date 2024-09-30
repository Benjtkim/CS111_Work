# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:52:08 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: Examples for module 8
"""
name = 'Jacob'
allcaps = name.upper()   # stores JACOB
reminder = 'Some Text Here!' 

def extract_results(filename, target_school):
    '''extracts the desired information from the file'''
    file = open(filename, 'r')
    
    for line in file:
        line = line[:-1]
        
        fields = line.split(',')
        athlete = fields[0]
        school = fields[1]
        event = fields[2]
        result = fields[3]
        
        if school == target_school:
            print(athlete, event, result)
        
    file.close()
    
def school_counts(filename):
    '''counts how many times a the name of a particular school appears in the 
    file'''
    file = open(filename, 'r')
    
    counts = {}
    
    for line in file:
        fields = line.split(',')
        
        school = fields[1]
        if school not in counts:
            counts[school] = 1
        else:
            counts[school] += 1
        
    file.close()
        
    print('There are', len(counts), 'schools in all.')
    for school in counts:
        print(school, 'has', counts[school], 'results.')

if __name__ == '__main__':
    
    #Examples calling string methods:
    print(allcaps)
    print(reminder.lower())   #prints some text here!
    print(reminder.replace('e','o'))   #prints Somo Toxt Horo!
    print(reminder.split())   #prints the list ['Some', 'Text', 'Here!']
    
    #extract_result test case.
    extract_results('schools.txt', 'BU')
    
    #school_counts test case.
    school_counts('schools.txt')
    