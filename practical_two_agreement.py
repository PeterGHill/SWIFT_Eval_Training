import plot_agreement as plotagr
import plot_spatial_rainfall as pltrain





valid_date = 20180628
start_time=0
end_time=24

latmin=-5
latmax=10
lonmin=-15
lonmax=10

#PLOTTING RAINFALL ACCUMULATIONS FOR OBS AND MODELS ON A MAP


#plotting GPM-IMERG on a map
pltrain.plot_rainfall_acc_scale_obs(valid_date,start_time,end_time,latmin,latmax,lonmin,lonmax)


init_date = #chose the date when the forecast is issued
init_time = #chose the initialization time of the forecast (this can be 0 or 12)
start_time = #this is the lead time (must be multiple of 3 since we have 3 hourly forecast)
end_time= #this has to be start_time+3,+6,+12,+24 depending which accumulation period you are considering

#plotting CP deterministic on a map
pltrain.plot_spatial_rainfall_acc_cp_model(init_date,valid_date,init_time,start_time,end_time,latmin,latmax,lonmin,lonmax)


#plotting global deterministic on a map
pltrain.plot_spatial_rainfall_acc_global_model(date,valid_date,init_time,start_time,end_time,latmin,latmax,lonmin,lonmax)





#PLOTTING AGREEMENT SCALE ON A MAP FOR THE TWO MODELS

alpha=#this is the tolerance factor and must be between 0 and 1
maxscale= #this the max number of grid points you want to investigate the agreement

plotagr.plot_spatial_map_of_agreement_scale_cp_model(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)


plotagr.plot_spatial_map_of_agreement_scale_global_model(alpha,maxscale,valid_date,init_date,init_time,start_time_mod,end_time_mod,start_time_obs,end_time_obs,latmin,latmax,lonmin,lonmax)
