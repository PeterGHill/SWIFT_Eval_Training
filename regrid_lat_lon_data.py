from scipy.interpolate import griddata
import numpy as np


def regrid(lat, lon, data, method='cubic', new_lat=np.arange(0.5,30), new_lon=np.arange(-19.5,20), min_val=0.0):
#   Note, this assumes that data.shape = (lat, lon) or (:, lat, lon).
    data_shape = data.shape
    n_lon = new_lon.size
    n_lat = new_lat.size
    if ((lon.ndim == 1) and (lat.ndim ==1)):
        lat, lon = np.meshgrid(lat, lon)
    points = np.dstack((lat.flatten(), lon.flatten()))[0,:,:]
    x1,x2 = np.meshgrid(new_lat, new_lon)
    new_points = np.dstack((x1.flatten(), x2.flatten()))[0,:,:]
    if data.ndim == 2:
        values = data.flatten()
        ind = np.where(values >= min_val)
        values = values[ind]
        points = points[ind]
        result = griddata(points, values, new_points, method=method, fill_value=-np.NaN).reshape(n_lat, n_lon) # works for gerb
    else:
        result = []
        for i in range(data_shape[0]):
            values = data[i,:,:].flatten()
            result += [griddata(points, values, new_points, method=method, fill_value=-np.NaN).reshape(n_lat, n_lon)]
        result = np.array(result) # works for era-interim
    return result


def average_regrid(lon, lat, data, new_lat=np.arange(0.5,30), new_lon=np.arange(-19.5,20), min_val=0.0, times_n = 1):
    data[data < min_val] = np.nan
    lat_bin_size = new_lat[1]-new_lat[0]
    lon_bin_size = new_lon[1]-new_lon[0]
    if times_n > 1:
        result = np.zeros((times_n, new_lon.size, new_lat.size))
    else:
        result = np.zeros((new_lon.size, new_lat.size))
    for i in range(new_lat.size):
        for j in range(new_lon.size):
            ind = np.where((abs(lon - new_lon[j]) <= lon_bin_size/2.0) &
                           (abs(lat - new_lat[i]) <= lat_bin_size/2.0))
            if times_n > 1:
                for k in range(times_n):
                    result[k, j, i] = np.nanmean(data[k,:,:][ind])
            else:
                result[j, i] = np.nanmean(data[ind])
    return result
