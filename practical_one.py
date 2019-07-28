'''
Code to run for the first practical exercise in the SWIFT evaluation workshop
Demonstrates how to load, manupulate and plot TAMSAT and GPM data.
Focuses on 26-30 June 2018
'''

import numpy as np
import open_plot_TAMSAT_netCDF
import plotting_routines
import read_gpm
import regrid_lat_lon_data
import datetime

# Load TAMSAT daily data. Load different days by editing the filename.
filename = r"C:\Users\PeterHill\SWIFT_Eval_Practical\TAMSAT\rfe2018_06_28.v3.nc" # Need to change to match the location of the file on your computer. 
t_rain, t_lat, t_lon, t_datevar = open_plot_TAMSAT_netCDF.open_TAMSAT_netCDF(filename)

# Plot TAMSAT map
plotting_routines.plot_map(t_rain.mean(axis=0), t_lat, t_lon, cbar_levels=np.arange(0,90,10), savename='TAMSAT_rainfall_map_28June2018.png') # Change savename as approrpitate

# Load GPM data.
# ********NB need to change gpm_dir in read_gpm.py for this to work********************
start_time = datetime.datetime(2018,6,28,0,0,0)
end_time = datetime.datetime(2018,6,28,23,30,0,0)
lon_min = -25. # West boundary of domain
lon_max = 55. # East boundary
lat_min = -15. # South boundary
lat_max = 25. # North boundary
g_rain, g_lat, g_lon, g_datevar = read_gpm.read_gpm(start_time, lon_min, lon_max, lat_min, lat_max, end_time=end_time)

# Plot GPM map
plotting_routines.plot_map(g_rain.mean(axis=0) * 24., g_lat, g_lon, cbar_levels=np.arange(0,90,10), savename='GPM_IMERG_rainfall_map_28June2018.png', title='GPM IMERG Rainfall') # Change savename as approrpitate

# Load GPM data around Kumasi and plot GPM diurnal cycle
g_rain_kumasi, g_lat_kumasi, g_lon_kumasi, g_datevar_kumasi = read_gpm.read_gpm(start_time, 1.6, 1.7, 6.6, 6.7, end_time=end_time)
plotting_routines.timeseries_plot(g_rain_kumasi.mean(axis=(1,2)), g_datevar_kumasi, 'Rainfall (mm h1-1)', savename='Kumasi_GPM_diurnal_cycle_28June2018.png')

# regrid both datasets to same resolution
new_res = 1.0 # new resolution in degrees change to look at how differences change with averaging scales
new_lat = np.arange(0.0, 20.0, new_res)
new_lon = np.arange(-15., 15., new_res) # regridding is slow so focus onreduced domain
regridded_g_rain = regrid_lat_lon_data.average_regrid(g_lat, g_lon, g_rain.mean(axis=0), new_lat=new_lat, new_lon=new_lon, min_val=0.0)
ind_lon = np.where((t_lon >= new_lon.min()) & (t_lon <= new_lon.max()))[0]
ind_lat = np.where((t_lat >= new_lat.min()) & (t_lat <= new_lat.max()))[0]
regridded_t_rain = regrid_lat_lon_data.average_regrid(t_lat[ind_lat], t_lon[ind_lon], t_rain.mean(axis=0)[ind_lat,:][:,ind_lon], new_lat=new_lat, new_lon=new_lon, min_val=0.0)


# Plot TAMSAT, GPM and difference maps at new resolution
plotting_routines.plot_map(regridded_t_rain, new_lat, new_lon, cbar_levels=np.arange(0,90,10), savename='Regridded_TAMSAT_rainfall_map_28June2018.png') # Change savename as approrpitate
plotting_routines.plot_map(regridded_g_rain * 24., new_lat, new_lon, cbar_levels=np.arange(0,90,10), savename='Regridded_GPM_IMERG_rainfall_map_28June2018.png') # Change savename as approrpitate
difference = regridded_t_rain - (regridded_g_rain * 24.)
plotting_routines.plot_map(difference, new_lat, new_lon, savename='TAMSAT_minus_GPM_rainfall_map_28June2018.png') # Change savename as approrpitate

# Scatterplot comparison, incuding correlations
plotting_routines.scatter_plot(regridded_t_rain, regridd_g_rain * 24., 'TAMSAT rainfall (mm day-1)', 'GPM IMERG Rainfall (mm day-1)', savename='TAMSAT_GPM_scatterplot_28June2018.png')
