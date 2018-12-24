#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 19:46:36 2018

@author: dinesh
"""

import math as mat

# the input for 'radians' function is degrees
def app(x):
    x = mat.radians(x)
    num = (16*(mat.pi-float(x)))*float(x)
    denom = (5*(mat.pi)**2)-((4*(mat.pi-float(x)))*float(x))
    return abs(num)/abs(denom)

print("Approximated sine value")
print(app(20))

print("Actual sine value")
print(mat.sin(mat.radians(90)))

# the input for 'degrees' function is radians
y = mat.degrees(mat.pi)
print("pi radians is 180 degrees")
print(y)

