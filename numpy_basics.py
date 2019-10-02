#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 08:37:21 2018

@author: dinesh
"""

import numpy as np

data1 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data1)
data1.__class__
arr1.__class__

# checking for features in numpy
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

# creating 3 rows & 6 columns with value '0'
a = np.zeros((3,6))
print(a)

# two (3*4) arrays with value 1
b = np.ones((2,3,4)) 
print(b)

# arange(15) goes from 0 to 14, reshaping in 3 rows & 5 columns
c = np.arange(15).reshape(3,5)
print(c)

# axis=1 is row slicing starting with index 0,1,2...
# axis=2 is column slicing starting with index 0,1,2...
d = np.arange(24).reshape(2,3,4)
print(d)

# for single column and any number of rows
e = np.arange(3).reshape(-1,1)
print(e)

# consider 2 arrays as index 0(1st 3*4) and index 1(2nd 3*4)
print(d[1,2,3]) 

# Tranpose
print(d.T)

# Square Root
print(np.sqrt(c))

# Exponential
print(np.exp(c))

# >=
x1 = [4,2,1]
x2 = [2,2,2]
print(np.greater_equal(x1,x2))

# Mod
print(np.mod(x1,x2))

# Initializing arrays with BOOLEAN tyle values
x1 = [True,False,True,False]
x2 = [True,True,False,False]
print(np.logical_and(x1,x2)) # Logical AND
print(np.logical_or(x1,x2)) # Logical OR

# Mean
print(c.mean())

# Standard Deviation
print(c.std())

# combining arrays
# axis = 1 => new columns
a = np.array([[1,2,3],[4,5,6]])
z = np.zeros((2,1))
print(np.append(a,z,axis=1))

# axis = 0 -> new rows
a = np.array([[1,2,3],[4,5,6]])
z = np.zeros((2,3))
print(np.append(a,z,axis=0))

# concatenate
arr = np.arange(12).reshape(3,4)
arr_con1 = np.concatenate([arr,arr],axis=1)
arr_con0 = np.concatenate([arr,arr],axis=0)
print(arr_con1)
print(arr_con0)


###########
## NOTES ##
###########

# The difference between np.ndarray and np.array is that the former is the actual type, while the latter is a flexible ...
# ... shorthand function for constructing arrays from data in other formats. The TypeError comes your use of ...
# ... np.array arguments to np.ndarray, which takes completely different arguments (see docstrings)

# Well, numpy.array is just a convenience function to create an ndarray, it is not a class itself.

