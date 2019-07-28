import regridding_data as regrid
import netCDF4 as nc
import numpy as np


def reading_cp_model_data(date,init_time):


    filename='C:/Users/carlo/Documents/Summer_School_evaluation/Data/'+str(date)+'T'+str(init_time).rjust(2,'0')+'00'+'Z_TAFRICA2_takm4p4_protora1t_4203_128.nc'
    
    
    d=nc.Dataset(filename)
    
    precip=d.variables['stratiform_rainfall_flux']  #units are mm/s

    return precip




def reading_global_model_data(date,init_time):


    filename='C:/Users/carlo/Documents/Summer_School_evaluation/Data/'+str(date)+'T'+str(init_time).rjust(2,'0')+'00'+'Z_TAFRICA2_n1280_ga6_5216_128.nc'
    
    
    d=nc.Dataset(filename)
    
    precip=d.variables['precipitation_flux']  #units are mm/s, data are 3-hourly

    return precip



def cp_model_accumulation_regridded(date,init_time,start_time,end_time):

    precip=reading_cp_model_data(date,init_time)


    start_time=int(start_time/3.)
    end_time=int(end_time/3.)-1

    precipnew=np.sum(precip[start_time:end_time,:,:],axis=0)*3*3600 #this is to convert to mm/3h

    precipacc=regrid.regridding_cp_data(precipnew)
    

    return precipacc


def global_model_accumulation_regridded(date,init_time,start_time,end_time):

    precip=reading_global_model_data(date,init_time)


    start_time=int(start_time/3.)
    end_time=int(end_time/3.)-1

    precipnew=np.sum(precip[start_time:end_time,:,:],axis=0)*3*3600 #this is to convert to mm/3h

    precipacc=regrid.regridding_global_data(precipnew)
    

    return precipacc



