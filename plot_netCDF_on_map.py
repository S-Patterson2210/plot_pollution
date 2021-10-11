import netCDF4 as nc

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
v = ds.variables['v'][:]
um = ds.variables['um'][:]
vm = ds.variables['vm'][:]

map = Basemap(projection='merc',llcrnrlon=0.,llcrnrlat=-80.,urcrnrlon=360.,urcrnrlat=80.,resolution='h')

map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='linen', ocean_color='blue')


lons, lats = np.meshgrid(lon,lat)
x,y = map(lons,lats)

clevs = np.arange(0,100,5)
# cs = map.contour(x,y,u[0,0,:,:],clevs,colors='red',linewidths=1)
cs = map.quiver(lons,lats,u[0,0,:,:],v[0,0,:,:],latlon=True)
plt.show()
