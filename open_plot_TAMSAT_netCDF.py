# This code contain two functions
# one function opens the TAMSAT data 
# obtained from the TAMSAT data extractor
# in netCDF format
# and the other plots the mean
# it uses a number of netCDF libraries
# cartopy is used for map plotting

# Import the necessary libraries
import numpy as np

import netCDF4
from netCDF4 import netcdftime,num2date 

# Plotting libraries
import matplotlib.pyplot as plt
import cartopy
import matplotlib
matplotlib.rcParams.update({'font.size': 18})
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def open_TAMSAT_netCDF(file_name):
    """
    This function opens the TAMSAT netCDF data
    it uses the netCDF4 libraries
    file_name should be a string containing the filename
    it returns the rainfall data (3D array), lat, lon and time (all 1D arrays)
    the time array contain datetime objects
    """

    # Open netCDF4 file
    nc = netCDF4.Dataset(file_name)

    # Extract rain, lat, lon, time
    rfe = nc.variables['rfe'][:]
    lat = nc.variables['lat'][:]
    lon = nc.variables['lon'][:]
    time     = nc.variables['time'][:]

    # Convert time to meaningful information
    tunit    = nc.variables['time'].units 
    t_cal    = u"gregorian" # nc.variables['time'].calendar
    datevar  = (num2date(time,units = tunit,calendar = t_cal))

    # Return 
    return rfe, lat, lon, datevar


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def plot_mean_rainfall(rainfall_data,lat,lon):
    """
    This function plots a map showing the mean rainfall
    rainfall_data should be a 3D array with dimensions time|lat|lon
    lat should be a 1D array containing latitude values
    lon should be a 1D array containing longitude values
    a plot is produced
    """

    # Calculate mean rainfall (over time)
    # Returns a 2D array (lat,lon)
    mean_rainfall = np.nanmean(rainfall_data, axis=0)

    # Plot
    plt.figure()
    ax = plt.subplot(1,1,1, projection=cartopy.crs.PlateCarree())

    # Contours and colour bar
    cp=plt.contourf(lon, lat,mean_rainfall ,transform=cartopy.crs.PlateCarree(), cmap = 'Spectral', levels =np.arange(10),extend='max' )
    cbar = plt.colorbar(cp)
    cbar.set_label('mm/day')

    # Map features
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS)
    #ax.add_feature(cartopy.feature.OCEAN, facecolor='white')

    # Grid lines
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,linewidth=1, color='black', alpha=0.5, linestyle='--', xlocs=np.arange(int(np.min(lon)),int(np.max(lon))+3,2))
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    # Extent and title
    ax.set_extent((np.min(lon),np.max(lon),np.min(lat),np.max(lat)), crs=cartopy.crs.PlateCarree())
    plt.title('TAMSAT Rainfall')

    plt.show()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Code to check this work
if __name__=='__main__':
    rfe, lat, lon, datevar = open_TAMSAT_netCDF('01-tamsatDaily.v3-946684800-1325376000_nir.nc')
    plot_mean_rainfall(rfe,lat,lon)
