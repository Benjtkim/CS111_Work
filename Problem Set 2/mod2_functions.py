# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:29:14 2024

@author: benjt
"""

def func(variable):
    local_variable = 3
    return variable*local_variable

global_variable = 5

print(func(global_variable))

def foo(variable):
    x = 7
    return x + variable

x = 5

print(foo(x))

