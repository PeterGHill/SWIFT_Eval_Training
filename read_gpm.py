'''
Read GPM calibrated precipitation for given area and time period
'''

def read_gpm(start_time, lon_min, lon_max, lat_min, lat_max, end_time=start_time, varname=''):
    '''
    Reads GPM precipitation data into an array with dimensions time, lat, lon
    '''
    return times, lons, lats, rain


def get_gpm_filelist():
    '''
    Given a time interval, generates list of GPM files that containg the data.
    Note this depends on the directory structure in place.
    '''
    return filelist

