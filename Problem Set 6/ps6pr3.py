#
# ps6pr3.py (Problem Set 6, Problem 3)
#
# Estimating pi
#
# Computer Science 111
# Date: 7/21/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: In this problem, I use a definite loop and an indefinite loop
# to estimate pi and the number of iterations it would take to get a 
# satisfactory estimation of pi.

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###
def for_pi(n):
    '''Using the throw_dart helper function, estimates the value of pi
    via a Monte-Carlo Simulation.'''
    
    #Accumulator varibles for darts thrown and darts hit.
    darts_thrown = 0
    darts_hit = 0
    
    #For loop that throws n darts.
    for throw in range(n):
        
        #If a throw hit inside the circle, increment both variables.
        if throw_dart() == True:
            darts_thrown += 1
            darts_hit += 1
            print(str(darts_hit) + ' hits out of ' + str(darts_thrown) + ' throws so that pi is ' + str((4 * darts_hit / darts_thrown)))

        #If not, increment solely darts_thrown. In both cases, we must print 
        #the statement shown.
        else:
            darts_thrown += 1
            print(str(darts_hit) + ' hits out of ' + str(darts_thrown) + ' throws so that pi is ' + str((4 * darts_hit / darts_thrown)))   
    
    #Return the estimate of pi.
    return (4 * darts_hit / darts_thrown)    

def while_pi(error):
    '''takes a positive floating-point input (error) and returns the number of 
    dart throws needed to produce an estimate of π that is less than error 
    away from the “actual” value of π'''
    #Accumulator varibles for darts thrown and darts hit.
    darts_thrown = 0
    darts_hit = 0
    while True:
        
        #If a throw hit inside the circle, increment both variables.
        if throw_dart() == True:
            darts_thrown += 1
            darts_hit += 1
            print(str(darts_hit) + ' hits out of ' + str(darts_thrown) + ' throws so that pi is ' + str((4 * darts_hit / darts_thrown)))
        
        #If not, increment solely darts_thrown. In both cases, we must print 
        #the statement shown.
        else:
            darts_thrown += 1
            print(str(darts_hit) + ' hits out of ' + str(darts_thrown) + ' throws so that pi is ' + str((4 * darts_hit / darts_thrown)))
        
        #Stops the loop if the estimate of pi is less than error away from the 
        #"actual" value of pi.
        if abs(math.pi - (4 * darts_hit / darts_thrown)) < error:
            return darts_thrown
            
            
if __name__ == '__main__':
    
    #for_pi test case.
    print(for_pi(100))
    
    #while_pi test case.
    print(while_pi(0.01))
        
        
            