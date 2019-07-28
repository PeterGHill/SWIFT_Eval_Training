'''
Includes various algorithms for identifying and labelling storms/clouds.
'''

import numpy as np
import scipy.ndimage as ndimage
from os.path import isfile

plot_dir = '/home/users/phill/tracking/'


def ltm(bt, minarea, threshold, struct, under_threshold=False):
    '''
    Code taken from Thorwald, uses a simple threhold to identify objects
    '''
    binbt=np.zeros_like(bt)
    if under_threshold:
        binbt[np.where(bt<threshold)]=1
    else:
        binbt[np.where(bt>threshold)]=1
    id_regions, num_ids = ndimage.label(binbt, structure=struct)
    id_sizes = np.array(ndimage.sum(binbt, id_regions, range(num_ids+1)))
    area_mask = (id_sizes < minarea)
    binbt[area_mask[id_regions]] = 0
    id_regions, num_ids = ndimage.label(binbt, structure=struct)
    print('num_ids = ',num_ids)
    
    return id_regions


def rdt(bt, minarea, struct, file_ID, Twarm=278., Tcold=203., deltaT=1.0):
    '''
    Use Rapid Developnment Thunderstorm algorithm method to identify storms
    '''
#   Initial label features with Twarm threshold
    binbt=np.zeros_like(bt)
    binbt[bt<Twarm]=1
    id_regions, num_ids = ndimage.label(binbt, structure=struct)
#   Get rid of features that are too small
    id_sizes = np.array(ndimage.sum(binbt, id_regions, range(num_ids+1)))
    area_mask = (id_sizes < minarea)
    binbt[area_mask[id_regions]] = 0
    id_regions, num_ids = ndimage.label(binbt, structure=struct)
#   Get rid of features that don't have a small enough min bt
    for i in range(1,num_ids+1):
        ind1 = np.where(id_regions == i)
        if (Twarm - bt[ind1].min() < 6.):
            binbt[ind1] = 0
    id_regions, num_ids = ndimage.label(binbt, structure=struct)    
#   Now increase temperature in deltaT increments and loop through 
#   each feature to check whether it can be split into two new feature using
#   this new temperature.
    for t in np.arange(Twarm, Tcold, -deltaT):
        binbt=np.zeros_like(bt)
        binbt[bt<t]=1
        id_regions_t, num_ids_t = ndimage.label(binbt, structure=struct)
        id_regions_t = id_regions_t.astype(float)
        id_regions_t[id_regions_t == 0.0] = np.nan
        new_regions = np.copy(id_regions)
        for i in range(1,num_ids+1):
            ind1 = np.where(id_regions == i)
            n_regions = np.unique(id_regions_t[ind1][~np.isnan(id_regions_t[ind1])]).size
            if n_regions > 1: # object has divided into subobjects!
                ind_list = []
                good_regions = np.zeros(n_regions)
                for j, region_id in enumerate(np.unique(id_regions_t[ind1][~np.isnan(id_regions_t[ind1])])):
                    ind2 = np.where(id_regions_t == region_id)
                    ind_list += [ind2]
                    if ((ind2[0].size > minarea) & (t - bt[ind2].min() > 6.)):
                        good_regions[j] = 1. # object works as stand alone storm
                good_ind = np.where(good_regions == 1)[0]
                if good_ind.size > 2:
                    new_regions[ind1] = 0
                    new_regions[ind_list[good_ind[0]]] = id_regions[ind1].max()
                    for ind in good_ind[1:]:
                        new_regions[ind_list[ind]] = num_ids +1
                        num_ids += 1
        id_regions = np.copy(new_regions)
    return id_regions


def label_storms(file_ID, method, time, domain, bt, minarea, struct, threshold=240., under_threshold=False, Twarm=278., Tcold=203., deltaT=1.0, plot_dir=plot_dir):
    '''
    Wrapper code reads and writes storm labels or calls appropriate labelling
    code if necessary
    '''
    filename = plot_dir + file_ID + '.npy'
    print "isfile(filename)=", isfile(filename)
    print "filename=", filename
    if isfile(filename):
        id_regions = np.load(filename)
    else:
        if method == 'threshold':
            id_regions = ltm(bt,minarea,threshold,struct, under_threshold=under_threshold)
        elif method == 'RDT':
            id_regions = rdt(bt,minarea,struct, Twarm=Twarm, Tcold=Tcold, deltaT=deltaT)
        else:
            print "Method ", method, " has not been coded! Exiting"
            STOP
        np.save(filename, id_regions)
    return id_regions
    
