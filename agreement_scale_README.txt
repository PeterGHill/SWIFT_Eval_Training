In this practical the aim is to find out at which scale (neighbourhood) the convection-permitting model is sufficiently similar to 
the observations. 
We will focus on the case of 26-30 June 2018 for West Africa.



#Steps for the calculation of the agreement scale

1. Regrid forecast data (convection-permitting and global model) to the observation grid using regrid_lat_lon.py function

2. Calculate rainfall accumulation for forecasts and observations for different accumulation period (forecast data 
   are 3-hourly (mm/h), observations are half-hourly (mm/h))

3. These two accumulations are the input of the agreement_scale.py function 


python files to be considered:

agreement.py #in this file there are the functions to calculate the agreement scale for cp deterministic and global model

reading_gpm_data.py #this is to read the gpm data and to calculate accumulation for a particular day on a time period you chose

reading_model_data.py #this is to read cp and global model data and to calculate accumulation for a given initial time,lead time and time period of accumulation


PLOTTING FUNCTIONS	

plot_spatial_rainfall.py #this is to plot the spatial map of rainfall for obs and models

plot_agreement.py #this is to plot the spatial map of agreement scale for both cp and global model #to plot 1 map it should take 5-6 minutes, depending on your maxscale








Exercises:

The event to be considered is the heavy rainfall event in West Africa (02/02/2019), widespread heavy rainfall.

1. First of all plot*** a spatial map of forecast rainfall accumulation and gpm observations for different
   accumulation period (6 h, 12 h, 24 h) and forecast lead time (1 day, 2 days, 3 days) and for the two models.
   Which accumulation periods/forecast lead times look more similar for the different locations ? (this is just
   by subjective comparison). Which model looks more similar to the observations ?


2. Calculate the agreement scale for these different accumulation periods and different lead times.
   Now you can ask the first question in a more objective way.

3. Which model is better ? In other words, which model has on average a smaller scale at which is similar to the 
   observed field ?
 

***To plot with Basemap you will need to install this in Anaconda. Type the following command in the Anaconda Prompt:
    conda install -c conda-forge basemap-data-hires=1.0.8.dev0
