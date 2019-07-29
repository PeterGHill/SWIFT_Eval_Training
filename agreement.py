import numpy

import netCDF4 as nc
import math
import numpy as np
import datetime as dt
import numpy.ma as ma

import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
import itertools
from scipy.signal import convolve2d
from scipy import ndimage
import scipy.interpolate
import reading_model_data as mod
import reading_gpm_data as gpm
import numpy.ma as ma

def distance_scale (f1, f2):
#14.06.2019
#this calculate the distance between f1, f2
#f1 and f2 are the observed and forecast rainfall
  if f1 > 0 or f2 > 0:
   D = (f1 - f2)**2/((f1)**2 +(f2)**2) 
  elif f1 == 0 and f2 == 0:
   D = 1
  return D 


def Dcrit (alpha, maxscale, scale):

#alpha and maxscale can be chosen by the user
#alpha measures the tolerance about different can be f1 and f2 and maxscale is the maximum scale we are
#investigating the similarity between the fields

   return alpha + (1 - alpha) * scale / maxscale 


def agreement_scale (f1, f2, alpha, maxscale, scale):

    D = distance_scale (f1, f2)
    Dcr = Dcrit(alpha, maxscale, scale) 
    if D<=Dcrit:
      return scale
         

def eight_neighbor_average_convolve2d (x, scale):
  kernel = np.ones ((scale * 2 + 1, scale * 2 + 1))
#this is to calculate the spatial average for each neighbourhood size
  neighbor_sum = ndimage.convolve (x, kernel, mode = 'reflect')
  num_neighbor = ndimage.convolve (np.ones (x.shape), kernel, mode = 'reflect') 
  return neighbor_sum / num_neighbor 


def agreement_scale_calculation_cp(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax):

  'in this code we calculate the agreement scale for the cp model'
   'alpha is the "tolerance factor", maxscale is the max number of grid points from the centre of neighbourhood you want to find similarity with obs'
  'init_date is the date when the forecast is issued'
  'init_time is the time when forecast is initialised (00 and 12 UTC only available)'
  'start_time_mod-end_time_mode is the lead time window you want to forecast the rainfall'
  'start_time_obs and end time obs are the times (UTC) of gpm-imerg accumulations'
   

  obs=gpm.obs_precip_accumulation_over_a_time_period(valid_date,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
  forecast=mod.cp_model_accumulation_regridded(init_date,init_time,start_time_mod,end_time_mod)

  'forecast are regridded to the same grid'
  
  indexlatobs,indexlonobs=gpm.domain_specification_obs(valid_date,latmin,latmax,lonmin,lonmax)



  agr_scale=np.zeros_like(obs)
  latcpa=indexlatobs[0]
  latcpb=indexlatobs[len(indexlatobs)-1]+1
  loncpa=indexlonobs[0]
  loncpb=indexlonobs[len(indexlonobs)-1]+1


  for s in range (maxscale, -1, -1):
      print ('Calculating agreement at scale',s)
      f1 = eight_neighbor_average_convolve2d(obs, s)
      f2 = eight_neighbor_average_convolve2d(forecast,s)
      f2=f2[latcpa:latcpb,loncpa:loncpb]

      f1=ma.masked_invalid(f1)
      f2=ma.masked_invalid(f2)
      for i in range (len (obs[:,0])): #this is to calculate the agreement scale at each point
        for j in range (len (obs[0,:])):

         if math.isnan(f2[i,j])==False: 
          if distance_scale(f1[i, j],f2[i, j])<=Dcrit(alpha, maxscale,s):
            
            agr_scale[i, j] = s
         else:
            agr_scale[i,j]=np.nan   
		      
  return agr_scale




def agreement_scale_calculation_global(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax):


  obs=gpm.obs_precip_accumulation_over_a_time_period(valid_date,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
  forecast=mod.global_model_accumulation_regridded(init_date,init_time,start_time_mod,end_time_mod)
  indexlatobs,indexlonobs=gpm.domain_specification_obs(valid_date,latmin,latmax,lonmin,lonmax)
  agr_scale=np.zeros_like(obs)
  latcpa=indexlatobs[0]
  latcpb=indexlatobs[len(indexlatobs)-1]+1
  loncpa=indexlonobs[0]
  loncpb=indexlonobs[len(indexlonobs)-1]+1
  for s in range (maxscale, -1, -1):
      print ('Calculating agreement at scale',s)
      f1 = eight_neighbor_average_convolve2d(obs, s)
      f2 = eight_neighbor_average_convolve2d(forecast,s)
      f2=f2[latcpa:latcpb,loncpa:loncpb]

      f1=ma.masked_invalid(f1)
      f2=ma.masked_invalid(f2)
      
      for i in range (len (obs[:,0])): #this is to calculate the agreement scale at each point
        for j in range (len (obs[0,:])):

          
          if math.isnan(f2[i,j])==False: 
           if distance_scale(f1[i, j],f2[i, j])<=Dcrit(alpha, maxscale,s):
            print ('agrscale',s) 
            agr_scale[i, j] = s
		      
  return agr_scale	

