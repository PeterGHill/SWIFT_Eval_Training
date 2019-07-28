# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:07:39 2016

@author: eebjw
"""

import numpy as np

def convert_binary(data,thresh):
    
    '''
    Return binary matrix whereby if data is above a threshold 1 is returned, otherwise 0
    
    Inputs:
        data = raw data e.g. precipitation values [lat,lon]
        thresh = rainfall threshold in mm (or kg m-2) e.g. 4 is a threshold of 4mm
        
    Outputs:
        I = binary matrix as described above [time,lat,lon]
    '''
    
    I = data[data?t]
    
    I = np.zeros(np.shape(data))

    for lat in range(np.shape(data)[0]):
        for lon in range(np.shape(data)[1]):
            if data[lat,lon] > thresh and data[lat,lon] > thresh_all:
                I[lat,lon] = 1
    return I  