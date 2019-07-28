#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:34:25 2017

@author: eebjw
"""

import numpy as np

def corner_count(I):

    '''
    Return matrix where the [i,j]th entry is the sum of all entries of the input matrix with i'<i and j'<j
    
    Inputs:
        I = binary matrix [lat,lon]
        
    Outputs:
        Z = summed matrix as described above [lat,lon]
    '''
    
    x_max = np.shape(I)[0]
    y_max = np.shape(I)[1]
    
    Z = np.zeros(np.shape(I))
    
    for x in range(x_max):
        for y in range(y_max):
            Z[x,y] = np.sum(I[0:x+1,0:y+1])
            
    return Z