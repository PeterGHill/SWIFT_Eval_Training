def plot_map(data,lat,lon, title='TAMSAT Rainfall', fig=plt.figure(), subplot='111', savename='', cbar_levels=np.arange(10), cbar_label='mm/day'):
    """
    This function plots a map showing the data
    data should be a 2D array with dimensions lat|lon
    lat should be a 1D array containing latitude values
    lon should be a 1D array containing longitude values
    a plot is produced
    """

    # Generate axes
    ax = fig.add_subplot(subplot, projection=cartopy.crs.PlateCarree())

    # Contours and colour bar
    cp=plt.contourf(lon, lat,mean_rainfall ,transform=cartopy.crs.PlateCarree(), cmap = 'Spectral', levels =cbar_levels,extend='max' )
    cbar = plt.colorbar(cp)
    cbar.set_label(cbar_label)

    # Map features
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS)
    #ax.add_feature(cartopy.feature.OCEAN, facecolor='white')

    # Grid lines
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,linewidth=1, color='black', alpha=0.5, linestyle='--', xlocs=np.arange(int(np.min(lon)),int(np.max(lon))+3,2))
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    # Extent and title
    ax.set_extent((np.min(lon),np.max(lon),np.min(lat),np.max(lat)), crs=cartopy.crs.PlateCarree())
    plt.title(title)

    if int(subplot[2]) == int(subplot[0])*int(subplot[1]):
        if savename != '':
            plt.savefig(savename)
        plt.show()

        
def scatter_plot(data1, data2, title1, title2, fig=plt.figure(), subplot='111', savename=''):
    # Generate axes
    ax = fig.add_subplot(subplot)
    plt.plot(data1, data2, 'ko')
    plt.xlabel(title1)
    plt.ylabel(title2)
    mean_diff = data1.mean() - data2.mean()
    correlation = np.corrcoef(data1, data2)
    rms_diff = np.sqrt(np.mean((data1-data2)**2))
    plt.text(0.25, 0.75, 'Difference='+mean_diff+'\nR2='+correlation+'\nRMSD='+rms_diff, horizontalalignment='left', verticalalignment='top',transform=ax.transAxes)
    if int(subplot[2]) == int(subplot[0])*int(subplot[1]):
        if savename != '':
            plt.savefig(savename)
        plt.show()

        
def timeseries_plot(data, time, varname, fig=plt.figure(), subplot='111', savename=''):
    ax = fig.add_subplot(subplot)
    plt.plot(time, data)
    plt.xlabel('Time')
    plt.ylabel(varname)
    if int(subplot[2]) == int(subplot[0])*int(subplot[1]):
        if savename != '':
            plt.savefig(savename)
        plt.show()
    
   
   
       
            
