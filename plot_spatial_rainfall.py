import reading_gpm_data as gpm
import agreement as agr
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap, shiftgrid,interp
import netCDF4 as nc
import numpy as np
import reading_model_data as mod
import plot_agreement as plot
import cartopy.crs as ccrs
import cartopy
import matplotlib
matplotlib.rcParams.update({'font.size': 18})
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.dates as mdates


def plot_rainfall_acc_scale_obs(date,start_time,end_time,latmin,latmax,lonmin,lonmax):

    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_'+str(date)+'.nc'
    d=nc.Dataset(filenameobs)
    latobs=d.variables['latitude']
    lonobs=d.variables['longitude']
    
    indexlatobs,indexlonobs=gpm.domain_specification_obs(date,latmin,latmax,lonmin,lonmax)
    

    
    latobs=latobs[indexlatobs]
    lonobs=lonobs[indexlonobs]

   
    
    latcpa=indexlatobs[0]
    latcpb=indexlatobs[len(indexlatobs)-1]+1
    loncpa=indexlonobs[0]
    loncpb=indexlonobs[len(indexlonobs)-1]+1
    
    
    


    
    title='GPM-IMERG accumulation on '+str(date)
    levels=np.linspace(0.1,50,10)
    obs=gpm.obs_precip_accumulation_over_a_time_period(date,start_time,end_time,latmin,latmax,lonmin,lonmax)

    fig=plt.figure()

    ax = plt.axes(projection=ccrs.PlateCarree())
    # Contours and colour bar
    cp=plt.contourf(lonobs, latobs,obs ,transform=ccrs.PlateCarree(), cmap = 'YlGnBu', levels =levels,extend='max' )
    cbar = plt.colorbar(cp)
    cbar_label=np.linspace(0,50,10)
    cbar.set_label(cbar_label)

    # Map features
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS)
    #ax.add_feature(cartopy.feature.OCEAN, facecolor='white')

    # Grid lines
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,linewidth=1, color='black', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    # Extent and title
    ax.set_extent((lonmin,lonmax,latmin,latmax), crs=cartopy.crs.PlateCarree())
    plt.title(title)
    
    
    plt.show()
    return


def plot_spatial_rainfall_acc_cp_model(date,valid_date,init_time,start_time,end_time,latmin,latmax,lonmin,lonmax):

    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_'+str(valid_date)+'.nc'
    d=nc.Dataset(filenameobs)
    latobs=d.variables['latitude']
    lonobs=d.variables['longitude']
    
    indexlatobs,indexlonobs=gpm.domain_specification_obs(valid_date,latmin,latmax,lonmin,lonmax)
    

    
    latobs=latobs[indexlatobs]
    lonobs=lonobs[indexlonobs]

   
    
    latcpa=indexlatobs[0]
    latcpb=indexlatobs[len(indexlatobs)-1]+1
    loncpa=indexlonobs[0]
    loncpb=indexlonobs[len(indexlonobs)-1]+1

    cp_precip=mod.cp_model_accumulation_regridded(date,init_time,start_time,end_time)[latcpa:latcpb,loncpa:loncpb]
   
    
    
   
    
    title='CP deterministic accumulation_init_date'+str(date)+'times_T+'+str(start_time)+'-'+str(end_time)
    
    fig=plt.figure()

    ax = plt.axes(projection=ccrs.PlateCarree())
    # Contours and colour bar
    levels=np.linspace(0.1,50,10)
    cp=plt.contourf(lonobs, latobs,cp_precip,transform=ccrs.PlateCarree(), cmap = 'YlGnBu', levels =levels,extend='max' )
    cbar = plt.colorbar(cp)
    cbar_label=np.linspace(0,50,10)
    cbar.set_label(cbar_label)

    # Map features
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS)
    #ax.add_feature(cartopy.feature.OCEAN, facecolor='white')
    
    # Grid lines
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,linewidth=1, color='black', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    # Extent and title
    ax.set_extent((lonmin,lonmax,latmin,latmax), crs=cartopy.crs.PlateCarree())
    plt.title(title)

    plt.show()
    return


def plot_rainfall_acc_global_model(date,valid_date,init_time,start_time,end_time,latmin,latmax,lonmin,lonmax):

    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_'+str(valid_date)+'.nc'
    d=nc.Dataset(filenameobs)
    latobs=d.variables['latitude']
    lonobs=d.variables['longitude']
    
    indexlatobs,indexlonobs=gpm.domain_specification_obs(valid_date,latmin,latmax,lonmin,lonmax)
    

    
    latobs=latobs[indexlatobs]
    lonobs=lonobs[indexlonobs]

   
    
    latcpa=indexlatobs[0]
    latcpb=indexlatobs[len(indexlatobs)-1]+1
    loncpa=indexlonobs[0]
    loncpb=indexlonobs[len(indexlonobs)-1]+1
    
    
    x,y,m=plot.mapProjection(lonobs,latobs,latmin,latmax,lonmin,lonmax,res='i')
    
    
   
    glob_precip=mod.global_model_accumulation_regridded(date,init_time,start_time,end_time)[latcpa:latcpb,loncpa:loncpb]
    
    
    fig=plt.figure()

    ax = plt.axes(projection=ccrs.PlateCarree())
    # Contours and colour bar
    levels=np.linspace(0.1,50,10)
    cp=plt.contourf(lonobs, latobs,glob_precip,transform=ccrs.PlateCarree(), cmap = 'YlGnBu', levels =levels,extend='max' )
    cbar = plt.colorbar(cp)
    cbar_label=np.linspace(0,50,10)
    cbar.set_label(cbar_label)

    # Map features
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS)
    #ax.add_feature(cartopy.feature.OCEAN, facecolor='white')

    # Grid lines
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,linewidth=1, color='black', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    # Extent and title
    ax.set_extent((lonmin,lonmax,latmin,latmax), crs=cartopy.crs.PlateCarree())
    plt.title(title) 
    return


