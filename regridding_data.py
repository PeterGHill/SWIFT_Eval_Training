import netCDF4 as nc
import scipy.interpolate
import numpy as np

def regridding_cp_data(old_grid_data):#03.07.2019


    'here we want to regrid cp_model data to observation grid'
    
    'we need only the dimensions of the old grid (cp model) and the dimensions of the new grid (cp model)'
    

    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_20180628.nc'
    
    filenamecp='C:/Users/carlo/Documents/Summer_School_evaluation/Data/20190202T0000Z_TAFRICA2_takm4p4_protora1t_4203_0.nc'
    
    
    dobs=nc.Dataset(filenameobs)
    dcp=nc.Dataset(filenamecp)

    
    latobs=dobs.variables['latitude']
    lonobs=dobs.variables['longitude']
    
    latcp=dcp.variables['latitude']
    loncp=dcp.variables['longitude']
    

    loncpnew=np.zeros(len(loncp))
    
    loncpnew[:]=loncp[:]-360
    
    
    
    #old grid
    X, Y = np.meshgrid(loncpnew, latcp)
    
    #new grid
    XI, YI = np.meshgrid(lonobs,latobs)

    #interp
    new_grid=scipy.interpolate.griddata((X.flatten(),Y.flatten()),old_grid_data.flatten() , (XI,YI),method='linear')

     
    return new_grid





def regridding_global_data(old_grid_data):



    'here we want to regrid cp_model data to observation grid'
    
    'we need only the dimensions of the old grid (cp model) and the dimensions of the new grid (cp model)'
    

    filenameobs='C:/Users/carlo/Documents/Summer_School_evaluation/Data/gpm_imerg_production_V06B_20180628.nc'
    
    filenameglobal='C:/Users/carlo/Documents/Summer_School_evaluation/Data/20190202T0000Z_TAFRICA2_n1280_ga6_5216_128.nc'
    
    
    dobs=nc.Dataset(filenameobs)
    dglob=nc.Dataset(filenameglobal)
    
    latobs=dobs.variables['latitude']
    lonobs=dobs.variables['longitude']
    
    latglob=dglob.variables['latitude']
    longlob=dglob.variables['longitude']
    

    longlobnew=np.zeros(len(longlob))
    
    longlobnew[:]=longlob[:]-360
    
    
    
    #old grid
    X, Y = np.meshgrid(longlobnew, latglob)
    
    #new grid
    XI, YI = np.meshgrid(lonobs,latobs)

    #interp
    new_grid=scipy.interpolate.griddata((X.flatten(),Y.flatten()),old_grid_data.flatten() , (XI,YI),method='linear')

     
    return new_grid
    
