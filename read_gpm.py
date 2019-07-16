'''
Read GPM calibrated precipitation for given area and time period
'''

from netCDF4 import Dataset
import numpy as np

gpm_dir = '/gws/nopw/j04/swift/GPM/' # Directory on Jasmin, will need to change.
gpm_res = 0.1


def read_gpm(start_time, lon_min, lon_max, lat_min, lat_max, end_time=-9999, varname='precipitationCal'):
    '''
    Reads GPM precipitation data into an array with dimensions time, lat, lon
    '''
    if end_time == -9999: end_time = start_time
    n_lon = int((lon_max - lon_min) / gpm_res)
    n_lat = int((lat_max - lat_min) / gpm_res)
    times, filelist = get_gpm_filelist(start_time, end_time)
    rain = np.zeros((len(times), n_lon, n_lat))
    for i, f in enumerate(filelist):
        ncfile = Dataset(f)
        lons = ncfile.variables['lon'][:]
        lats = ncfile.variables['lat'][:]
        ind_lon = np.where((lon >= lon_min) & (lon <= lon_max))[0]
        ind_lat = np.where((lat >= lat_min) & (lat <= lat_max))[0]
        if ncfile.variables[varname].ndim == 3: # Some GPM files have an extra dimension - don't understand why
            rain[i,:,:] = ncfile.variables[varname][0,ind_lon[0]:ind_lon[-1]+1, ind_lat[0]:ind_lat[-1]+1]
        elif ncfile.variables[varname].ndim == 2:
            rain[i,:,:] = ncfile.variables[varname][ind_lon[0]:ind_lon[-1]+1, ind_lat[0]:ind_lat[-1]+1]
        else:
            print varname, "has", ncfile.variables[varname].ndim, "dimensions, which is beyond the scope of this code"
    rain = np.ma.masked_array(rain, mask=(rain < 0.0))
    return times, lons[ind_lon], lats[ind_lat], rain


def get_gpm_filelist(start_time, end_time):
    '''
    Given a time interval, generates list of GPM files that containg the data.
    Note this depends on the directory structure in place.
    '''
    n_times = (end_time - start_time).total_seconds() / (60 * 30.) + 1
    timelist = [start_time + datetime.timedelta(seconds=60 * 30. * n) for n in n_times]
    filelist = []
    for time in timelist:
        f += [glob.glob(gpm_dir + time.strftime('%Y/%m/%d/*%Y%m%d-S%H%M*.nc'))] # Note assumes only one file for each timestamp
    return timelist, filelist

