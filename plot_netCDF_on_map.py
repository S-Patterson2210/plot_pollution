import netCDF4 as nc
# from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits
from mpl_toolkits.basemap import Basemap

ds = nc.Dataset('oscar_vel10004.nc')
vars = ds.variables
for v in vars:
    print (v)


lat = ds.variables['latitude'][:]
lon = ds.variables['longitude'][:]
time = ds.variables['time'][:]
depth = ds.variables['depth'][:]
u = ds.variables['u'][:]

map = Basemap(projection='merc',llcrnrlon=0.,llcrnrlat=-80.,urcrnrlon=360.,urcrnrlat=80.,resolution='c')

map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='linen', ocean_color='blue')


lons, lats = np.meshgrid(lon,lat)
x,y = map(lons,lats)

clevs = np.arange(0,100,5)
cs = map.contour(x,y,u[0,0,:,:],clevs,colors='red',linewidths=1)

plt.show()





