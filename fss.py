#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:30:56 2019

@author: eebjw
"""

import numpy as np
import iris
from cube_extract import cube_extract
from four_corners import four_corners
from corner_count import corner_count
from compute_fss import compute_fss
import matplotlib.pyplot as plt
from plot_map import plot_map
import cartopy.crs as ccrs
import sys

lat_min = 3
lat_max = 20
lon_min = -40
lon_max = -5
proj = ccrs.PlateCarree(central_longitude=0) # projection for maps

'''four corners or 'fast' method: http://metnet.imd.gov.in/mausamdocs/166310_F.pdf'''

def main():
    
    '''Step 1: Load data'''
    fpath = '/Users/eebjw/Downloads/fss_practical/'
    fname_obs = fpath+'gpm_imerg_production_V06B_20180626_1800.nc' # path to observations
    obs = iris.load(fname_obs)[0] # load observational data
    model = 'takm4p4_protora1t' # model name for CP model, note that global model name is 'n1280_ga6'
    fname_mod = fpath+'20180626T0000Z_TAFRICA2_'+model+'_128_20180626_1800.nc' # path to model data
    mod = iris.load(fname_mod)[0] # load model data
    
    '''Step 2: Regrid to largest grid-spacing and crop to area of interest'''
    mod = mod.regrid(obs, iris.analysis.Linear()) # re-grid model data to the same grid as the observational data
    obs = cube_extract(obs,lat_min,lat_max,lon_min,lon_max) # extract obs within lat and lon bounds
    mod = cube_extract(mod,lat_min,lat_max,lon_min,lon_max) # extract model within lat and lon bounds 
    
    print (obs)
    print (mod)
    
    print (obs.units)
    print (mod.units)
    
    sys.exit()
    
    '''Step 3: Make units the same'''
    mod.convert_units('kg m-2 h-1')
    
    '''Plot data to compare by eye'''
    fig = plt.figure(figsize=(8,5))
    cmap = plt.cm.jet
    cmap.set_under('white')
    levels =[0.1,0.2,0.5,1,2,5,10,20,50]
    X,Y = np.meshgrid(obs.coord('longitude').points,obs.coord('latitude').points) # create X and Y coordinates
    ax = plt.subplot(121,projection=proj) # set up subplot for observational data
    ax,im = plot_map(ax,X,Y,obs.data,cmap,levels) # plot observational data
    ax.set_title('Observations')
    bx = plt.subplot(122,projection=proj) # set up subplot for model data
    bx,im = plot_map(bx,X,Y,mod.data,cmap,levels) # plot model data
    bx.set_title('Model')
    cbar_ax = fig.add_axes([0.1, 0.1, 0.8, 0.03]) # create axis for colorbar
    cbar = fig.colorbar(im, cax=cbar_ax,orientation='horizontal') # add colorbar
    cbar.set_label('precipitation rate (mm h$^{-1}$)') # label colorbar
    plt.subplots_adjust(bottom=0.19,top=0.99) # adjust layout to fit nicely
    plt.show()
    
    '''Step 4: Specify thresholds and neighbourhood sizes'''
    thresh = 0.5 # rainfall threshold ammount in mm (or kg m-2)
    ns = np.arange(1,51,2) # list of neighbourhood sizes
       
    '''Step 5: Convert to binary field - all grid squares exceeding the threshold have a value of 1 and all others a value of 0'''
    I_obs = obs.data>thresh
    I_mod = mod.data>thresh
    
    '''Plot binary fields'''
    fig = plt.figure(figsize=(8,5))
    cmap = plt.cm.viridis
    levels =[0,1,2]
    X,Y = np.meshgrid(obs.coord('longitude').points,obs.coord('latitude').points) # create X and Y coordinates
    ax = plt.subplot(121,projection=proj) # set up subplot for observational data
    ax,im = plot_map(ax,X,Y,I_obs,cmap,levels) # plot observational data
    ax.set_title('Observations')
    bx = plt.subplot(122,projection=proj) # set up subplot for model data
    bx,im = plot_map(bx,X,Y,I_mod,cmap,levels) # plot model data
    bx.set_title('Model')
    cbar_ax = fig.add_axes([0.1, 0.1, 0.8, 0.03]) # create axis for colorbar
    cbar = fig.colorbar(im, cax=cbar_ax,orientation='horizontal') # add colorbar
    cbar.set_label('precipitation rate (mm h$^{-1}$)') # label colorbar
    plt.subplots_adjust(bottom=0.19,top=0.99) # adjust layout to fit nicely
    plt.show()
    
    '''Step 6: Create summed area matrix for use in four corners method '''        
    Z_obs = corner_count(I_obs) # Compute summed-area matrix for obs
    Z_mod = corner_count(I_mod) # Compute summed-area matrix for model
    
    '''loop through neighbourhood sizes'''
    fss = []
    for n in ns:
        print (n)
        
        '''Step 7: Using four corners method, generate fractions from summed-area matrix for different n'''
        O = four_corners(Z_obs,n)
        M = four_corners(Z_mod,n)
        
        '''Step 8: Compute FSS'''
        fss.append(compute_fss(M,O))
        
    ax = plt.subplot(111)
    ax.plot(ns,fss)
    ax.set_xlabel('neighbourhood size (grid boxes)')
    ax.set_ylabel('FSS')
    ax.axhline(y=0.5,color='k')
    plt.show()

if __name__ == '__main__':
    main()
