#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:04:38 2019

@author: eebjw
"""

import numpy as np
import cartopy.crs as ccrs
from matplotlib.colors import BoundaryNorm
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature

'''Setup for maps'''
proj = ccrs.PlateCarree(central_longitude=0)      
lakes_50m = cfeature.NaturalEarthFeature('physical', 'lakes', '50m',edgecolor='k',facecolor=cfeature.COLORS['water'])
land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m',edgecolor='k',facecolor='none')
countries_50m = cartopy.feature.NaturalEarthFeature('cultural','admin_0_countries','50m',edgecolor='k',facecolor='none')

def plot_map(ax,data,cmap,levels):
    
    X,Y = np.meshgrid(data.coord('longitude').points,data.coord('latitude').points) # create X and Y coordinates
    
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=False)
    ax.set_extent([np.min(data.coord('longitude').points), np.max(data.coord('longitude').points), np.min(data.coord('latitude').points), np.max(data.coord('latitude').points)], proj)
    ax.coastlines('50m')
    ax.add_feature(land_50m, linewidth=0.5)
    ax.add_feature(countries_50m, linewidth=0.5) 
    ax.add_feature(lakes_50m, linewidth=0.5)
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
    gl.xlines = False
    gl.ylines = False
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xlabel_style = {'size': 6, 'rotation': 90}
    gl.ylabel_style = {'size': 6}
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    im = ax.pcolormesh(X, Y, data.data, cmap=cmap, norm=norm)
    
    return ax,im