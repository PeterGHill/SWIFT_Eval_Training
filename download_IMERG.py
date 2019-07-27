'''
Downloads GPM IMERG data. Note only hdf5 format is available from
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


def ftp_data(latency, gpm_datelist):
    '''
    Use ftp to download files in gpm_filelist
    '''
    try:
       ftp = ftplib.FTP(server[latency][0], user=server[latency][1], password=server[latency][2])
        print " ... connecting to the IMERG-DB"
    except:
        print(" !!FTP Connection Failed -> ", server[latency][0])
    new_gpm_filelist = []
    for gpm_date in gpm_datelist:
        year, month, day = getYMD(single_date)
        sfilepath = {'Final' : '/gpmdata/'+year+'/'+month+'/'+day+'/imerg/3B-HHR.MS.MRG.3IMERG.',
                     'NRTlate' : '/NRTPUB/imerg/late/'+year+month+'/3B-HHR-L.MS.MRG.3IMERG.'+year+month+day,
                     'NRTearly': '/NRTPUB/imerg/early/'+year+month+'/3B-HHR-E.MS.MRG.3IMERG.'+year+month+day} 
       gpm_filelist = ftp.nlist(sfilepath[latency]+'*.RT-H5')
       rawdata_dir = my_gpm_data_dir+'IMERG/'+latency+'/'+year+'/'+month+'/'+day
       for gpm_file in gpm_filelist
           try:
               ftp.retrbinary('RETR %s' % gpm_file, open(sfilepath[latency]+ntpath.basname(gpm_file), 'wb').write)
           except:
               print "no such gpm imerg directory in ftp server", gpm_file
               ftp.quit()
           else:
               new_gpm_filelist += [sfilepath[latency]+ntpath.basname(gpm_file)]
    ftp.quit()
    return new_gpm_filelist


def download_gpm(start_date='27072019', end_date=-9999, var = 'precipitationCal', latency='Final'):
    start_date = datetime.datetime.strptime(start_date, '%d%m%Y')
    if end_date == -9999:
          datelist = [start_date]
    else:
        end_date = datetime.datetime.strptime(end_date, '%d%m%Y')
        n_days = 1 + (end_date - start_date).total_seconds() / (60*60*24.)
        datelist =  [start_date + datetime.timedelta(days=d) for d in range(int(n_days))]
    rawdatafiles = ftp_data(latency, datelist)
