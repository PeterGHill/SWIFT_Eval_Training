'''
Code to run for the first practical exercise in the SWIFT evaluation workshop
Demonstrates how to load, manupulate and plot TAMSAT and GPM data.
Focuses on 26-30 June 2018
'''

import numpy as np
import open_plot_TAMSAT_netCDF
import plotting_routines
import read_gpm

# Load TAMSAT daily data. Load different days by editing the filename.
filename = r"C:\Users\PeterHill\SWIFT_Eval_Practical\TAMSAT\rfe2018_06_28.v3.nc" # Need to change to match the location of the file on your computer. 
t_rain, t_lat, t_lon, t_datevar = open_plot_TAMSAT_netCDF.open_TAMSAT_netCDF(filename)

# Plot TAMSAT map
plotting_routines.plot_map(t_rain.mean(axis=0), t_lat, t_lon, savename='TAMSAT_rainfall_map_28June2018.png') # Change savename as approrpitate

# Load GPM data
start_time=datetime.datetime()
end_time=datetime.datetime()
lon_min= # West boundary of domain
lon_max=
lat_min=
lat_max
g_rain, g_lat, g_lon, g_datevar = read_gpm.read_gpm(start_time, lon_min, lon_max, lat_min, lat_max, end_time=end_time)

# Plot GPM map
plotting_routines.plot_map(g_rain.mean(axis=0), g_lat, g_lon, savename='GPM_IMERG_rainfall_map_28June2018.png') # Change savename as approrpitate


# regrid both datasets to same resolution


# Plot TAMSAT, GPM and difference maps at new resolution


# Scatterplot comparison, incuding correlations



# 
