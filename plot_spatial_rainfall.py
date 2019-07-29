import reading_gpm_data as gpm
import agreement as agr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid,interp
import netCDF4 as nc
import numpy as np
import reading_model_data as mod
import plot_agreement as plot

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
    
    
    x,y,m=plot.mapProjection(lonobs,latobs,latmin,latmax,lonmin,lonmax,res='i')
    
    
   
    obs=gpm.obs_precip_accumulation_over_a_time_period(date,start_time,end_time,latmin,latmax,lonmin,lonmax)
    
    
    N_bands=7
    levels= np.linspace(0, 100, num=N_bands+1) 
    plt.contourf(x,y,obs,levels,cmap='YlGnBu',vmin=0,vmax=100,extend='max')
    #m.plot(xN,yN,'bo',markersize=8)
    plt.colorbar(orientation='horizontal')
        
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
    
    
    x,y,m=plot.mapProjection(lonobs,latobs,latmin,latmax,lonmin,lonmax,res='i')
    
    
   
    cp_precip=mod.cp_model_accumulation_regridded(date,init_time,start_time,end_time)[latcpa:latcpb,loncpa:loncpb]
    
    
    N_bands=7
    levels= np.linspace(0, 100, num=N_bands+1) 
    plt.contourf(x,y,cp_precip,levels,cmap='YlGnBu',vmin=0,vmax=100,extend='max')
    #m.plot(xN,yN,'bo',markersize=8)
    plt.colorbar(orientation='horizontal')
        
    plt.show() 
    return


def plot_spatial_rainfall_acc_global_model(date,valid_date,init_time,start_time,end_time,latmin,latmax,lonmin,lonmax):

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
    
    
    N_bands=7
    levels= np.linspace(0, 100, num=N_bands+1) 
    plt.contourf(x,y,glob_precip,levels,cmap='YlGnBu',vmin=0,vmax=100,extend='max')
    #m.plot(xN,yN,'bo',markersize=8)
    plt.colorbar(orientation='horizontal')
        
    plt.show() 
    return


