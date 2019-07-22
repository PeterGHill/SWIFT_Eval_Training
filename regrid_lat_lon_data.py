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
