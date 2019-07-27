

#Steps for the calculation of the agreement scale

1. Regrid forecast data (convection-permitting and global model) to the observation grid using regrid_lat_lon.py function

2. Calculate rainfall accumulation for forecasts and observations for different accumulation period (forecast data 
   are 3-hourly (mm/h), observations are half-hourly (mm/h))

3. These two accumulations are the input of the agreement_scale.py function 

Exercises:

The event to be considered is the heavy rainfall event in West Africa (02/02/2019), widespread heavy rainfall.

1. First of all plot a spatial map of forecast rainfall accumulation and gpm observations for different
   accumulation period (6 h, 12 h, 24 h) and forecast lead time (1 day, 2 days, 3 days) and for the two models.
   Which accumulation periods/forecast lead times look more similar for the different locations ? (this is just
   by subjective comparison). Which model looks more similar to the observations ?


2. Calculate the agreement scale for these different accumulation periods and different lead times.
   Now you can ask the first question in a more objective way.

3. Which model is better ? In other words, which model has on average a smaller scale at which is similar to the 
   observed field ?
 

