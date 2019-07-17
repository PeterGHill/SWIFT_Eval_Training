# This code opens and plots the data from a csv file  
# obtained from the TAMSAT data extraction tool
# it uses the numpy and matplotlib libraries
# and the csv and datetime libraries
# this code is written to work in Python2.7

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import datetime 
import csv 

# This changes the size of the font used in the plot
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

# Define the file name (and location)
# INSERT FILENAME HERE
file_name = '01-tamsatDaily.v3-1514764800-1559343600_gha.csv'#'01-tamsatDaily.v3-1325376000-1483228800_gha.csv'

# Open the file 
open_file  = open(file_name)
csv_output = csv.reader(open_file)

# Extract each line and separate into two arrays
dates = []
rain  = []
for line in csv_output: 

    # Ignore the column headings
    if line[0]=='time': 
        continue

    # Extract and convert the date and rainfall
    date       = line[0]
    dt_object  = datetime.datetime.strptime(date,'%d/%m/%Y')
    rain_value = float(line[1])

    # Append to arrays
    dates.append(dt_object)
    rain.append(rain_value)

# Remove any missing values (-999)
# Fill with NaN (not a number)
rain = np.array(rain)
rain[np.where(rain<-100)] = np.nan


# Plot
plt.figure()
plt.plot(dates,rain,lw=1.5, color='mediumblue')
plt.xlabel('Time')
plt.ylabel('Rainfall (mm)')
plt.title('TAMSAT rainfall over Ghana') # Change title
plt.xticks(rotation='90')
plt.grid()
plt.subplots_adjust(bottom=0.25)
plt.show()
