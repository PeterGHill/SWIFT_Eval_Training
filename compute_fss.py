# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:57:31 2016

@author: eebjw
"""

import numpy as np
from compute_mse import compute_mse
from compute_mse_ref import compute_mse_ref

def compute_fss(M,O):
    
    '''
    Compute FSS (see Roberts and Lean, 2008)
    
    Inputs:
        M = matrix of fractions for model
        O = matrix of fractions for model
        
    Outputs:
        fss = Fractions Skill Score
    '''
    
    
    mse = compute_mse(M,O) # compute mean square error between simulated and observed fraction
    mse_ref = compute_mse_ref(M,O) # compute mean square error of reference forecast
    
    fss = 1 - mse/mse_ref # compute fractions skill score
        
    return fss
    
