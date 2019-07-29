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
    
    
    x,y,m=mapProjection(lonobs,latobs,latmin,latmax,lonmin,lonmax,res='i')
    
    
   
    
    
    agreement_scale=agr.agreement_scale_calculation_cp(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
    
    
    
    N_bands=7
    levels= np.linspace(0, maxscale, num=N_bands+1) 
    plt.contourf(x,y,agreement_scale,levels,cmap='BuPu',vmin=0,vmax=maxscale,extend='max')
    #m.plot(xN,yN,'bo',markersize=8)
    plt.colorbar(orientation='horizontal')
        
    plt.show() 
    return





def plot_spatial_map_of_agreement_scale_global_model(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax):#24.06.2019

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
    
    
    x,y,m=mapProjection(lonobs,latobs,latmin,latmax,lonmin,lonmax,res='i')
    
    
   
    
    
    agreement_scale=agr.agreement_scale_calculation_global(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
    
    
    
    N_bands=7
    levels= np.linspace(0, maxscale, num=N_bands+1) 
    plt.contourf(x,y,agreement_scale,levels,cmap='BuPu',vmin=0,vmax=maxscale,extend='max')
    #m.plot(xN,yN,'bo',markersize=8)
    plt.colorbar(orientation='horizontal')
        
    plt.show() 
    
    return





def plot_agreement_scale_histograms_global(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax):    


    agrglobal=agr.agreement_scale_calculation_global(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
    agrcp=agr.agreement_scale_calculation_cp(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)

    agrglobal = agrglobal.ravel()
    agrcp=agrcp.ravel()
    
    

    bins=np.linspace(0, 20, 10)
    
    plt.hist([agrcp, agrglobal], bins, label=['CP', 'global'])

    plt.show()

    
def mapProjection(lons,lats,lata,latb,lona,lonb,res='i'):
    m = Basemap(width=1050000,height=1310000,projection='tmerc',lat_0 = (lata+latb)/2., lon_0 = (lona+lonb)/2.,llcrnrlat=lata,urcrnrlat=latb,llcrnrlon=lona,urcrnrlon=lonb,resolution=res)
    #map long and lat coords onto map projection

    plt.figure(figsize=(10,10))
    X,Y = np.meshgrid(lons, lats)
    x,y = m(X,Y)
    m.drawcoastlines(linestyle='-',linewidth=1.0)
    m.drawmapboundary(fill_color='#bfbfbf')
    parallels = np.arange(-90,90,2)
    m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
    meridians = np.arange(0.,360.,2)
    m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
    """m.drawparallels(np.arange(48,64,2),labels=[1,0,0,0], linewidth=0.5,dashes=[1,6])
    m.drawmeridians(np.arange(-10,10,2),labels=[0,0,0,1], linewidth=0.5,dashes=[1,6])"""
    return x,y,m
