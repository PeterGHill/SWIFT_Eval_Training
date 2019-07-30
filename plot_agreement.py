import reading_gpm_data as gpm
import agreement as agr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid,interp
import netCDF4 as nc
import numpy as np


def plot_spatial_map_of_agreement_scale_cp_model(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax):

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
    
    
    
    
    
   
    
    
    agreement_scale=agr.agreement_scale_calculation_cp(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
    
    
    title='Agreement scale CP deterministic_init_date'+str(init_date)+'accumulation_period_T+'+str(start_time_mod)+'-'+str(end_time_mod)

    levels=np.linspace(0,maxscale,10)
    cp=plt.contourf(lonobs, latobs,agreement_scale,transform=ccrs.PlateCarree(), cmap = 'YlGnBu', levels =levels,extend='max' )
    cbar = plt.colorbar(cp)
    cbar_label=np.linspace(0,maxscale,10)
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

