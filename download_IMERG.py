'''
Downloads GPM IMERG data, and converts to daily netCDF file.
'''

import ftplib
import os

# Need to register for access to GPM data through pps at
# https://registration.pps.eosdis.nasa.gov/registration/
# in order for this to work

# Variables to edit
email_address = '' # Enter the email address used to register for GPM access here.
my_gpm_data_dir = '' # Enter the location of the directory where GPM data will be stored

# Fixed variables
server = {'Final' : ['arthurhou.pps.eosdis.nasa.gov', email_address, '.HDF5'],
          'NRTlate'    : ['jsimpson.pps.eosdis.nasa.gov', email_address, '.RT-H5'],
          'NRTearly'   : ['jsimpson.pps.eosdis.nasa.gov', email_address, '.RT-H5']}
          

def getYMD(indate):
    year = indate.strftime("%Y")
    month = indate.strftime("%m")
    day = indate.strftime("%d")
    return(year, month, day)


