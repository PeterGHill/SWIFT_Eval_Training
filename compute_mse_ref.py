# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:39:58 2016

@author: eebjw
"""

import numpy as np

def compute_mse_ref(M,O):
    
    '''
    Compute reference mean square error (see Roberts and Lean, 2008)
    
    Inputs:
        M = matrix of fractions for model
        O = matrix of fractions for model
        
    Outputs:
        mse = reference mean square error between fractions in model and observations
    '''
    
    x = 0
    for i in range(np.shape(M)[0]):
        for j in range(np.shape(M)[1]):
            x = x + O[i,j]**2+M[i,j]**2
    mse_ref = x/(np.shape(M)[0]*np.shape(M)[1])
    
    return mse_ref