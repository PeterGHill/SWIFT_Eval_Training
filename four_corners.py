#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:34:25 2017

@author: eebjw
"""

from __future__ import division
import numpy as np

def four_corners(Z,n):
    
    '''
    Z: corner count (summed-area) matrix
    n: neighbourhood size
    
    At every point. find sum over surrounding neighbourhood of size n from summed-area table
    
    See: https://en.wikipedia.org/wiki/Summed-area_table
    
    '''
    
    x_max = np.shape(Z)[0]
    y_max = np.shape(Z)[1]
            
    frac = np.zeros(np.shape(Z))
    
    ins = (n-1)/2
    outs = (n+1)/2
    
    for x in range(x_max):
        for y in range(y_max):
            A_idx = [int(x+ins),int(y+ins)]
            if A_idx[0] > x_max-1:
                A_idx[0] = x_max-1
            if A_idx[1] > y_max-1:
                A_idx[1] = y_max-1
            A = Z[A_idx[0],A_idx[1]]
            B_idx = [int(x+ins),int(y-outs)]
            if B_idx[0] > x_max-1:
                B_idx[0] = x_max-1
            if B_idx[1] < 0:
                B = int(0)
            else:
                B = Z[B_idx[0],B_idx[1]]
            C_idx = [int(x-outs),int(y+ins)]
            if C_idx[1] > y_max-1:
                C_idx[1] = y_max-1
            if C_idx[0] < 0:
                C = int(0)
            else:
                C = Z[C_idx[0],C_idx[1]]
            D_idx = [int(x-outs),int(y-outs)]
            if D_idx[0] < 0 or D_idx[1] < 0:
                D = int(0)
            else:
                D = Z[D_idx[0],D_idx[1]]
                
            frac[x,y] = A-B-C+D
    
    frac = frac/(n*n)   
    return frac