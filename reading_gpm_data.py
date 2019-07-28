import netCDF4 as nc
import datetime as dt
import numpy as np

def reading_gpm_observations(date):

    
    
    
    filename='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_'+str(date)+'.nc'
    
    
    d=nc.Dataset(filename)
    
    precip=d.variables['precipitation_flux']  

    return precip



def domain_specification_obs(date,latmin,latmax,lonmin,lonmax):
    
    'here we specifiy the domain of our study, retrieving latitude and longitude indices from gpm observations'
    
    
    
    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_'+str(date)+'.nc' #you have change this path of course
    
    
    
    
    dobs=nc.Dataset(filenameobs)
   
    
    
    
    latobs=dobs.variables['latitude']
    lonobs=dobs.variables['longitude']
    
    
    
    
    
    indexlatobs=[i for i, e in enumerate(latobs) if latmin<=e<=latmax]
    indexlonobs=[i for i, e in enumerate(lonobs) if lonmin<=e<=lonmax]
    
              
    return indexlatobs,indexlonobs




def obs_precip_accumulation_over_a_time_period(date,start_time,end_time,latmin,latmax,lonmin,lonmax):

    #start_time and end_time must be given in LT (local time)



    precip=reading_gpm_observations(date)

    indexlatobs,indexlonobs=domain_specification_obs(date,latmin,latmax,lonmin,lonmax)

       


    


    
    times=np.arange(start_time*2,end_time*2)#*2 is because data are half hourly

    print (times)
    precip_domain=precip[:,indexlatobs,indexlonobs]


    
    precip_accumulation=np.zeros_like(precip_domain[0,:,:])
    
    
           #we are summing the two half hours together in the time period chosen and taking the average

    for i in range(len(precip_accumulation[:,0])):
       for j in range(len(precip_accumulation[0,:])):
           a=[]
           for s in range(len(times)-1):
            if s%2==0:
             a.append((precip_domain[times[s],i,j]+precip_domain[times[s+1],i,j])/2.)
           
           precip_accumulation[i,j]=np.sum(a)    
             
	 
	 
    
    #precip_accumulation=np.delete(precip_accumulation,np.s_[1::2],1)	    
     
    
    return precip_accumulation




