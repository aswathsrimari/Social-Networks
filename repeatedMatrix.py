# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:19:19 2019

@author: user
"""

import numpy
A=numpy.mat('1 2;3 4')
v=numpy.mat('1;1')
print(v)
print("********")
for i in range(10):
    z=A*v
    z=z/numpy.linalg.norm(z)  #normalization- pull to unit circle
    print(z)
    v=z 
    print("********")