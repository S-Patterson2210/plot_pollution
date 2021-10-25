import netCDF4 as nc

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits
from mpl_toolkits.basemap import Basemap

# The below line denotes which file I am pulling the data from
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

# Self explanatory but below is telling program to draw particulars of a map e.g coastlines
map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='linen', ocean_color='blue')

stride = 3

# Meshgrid tells the code to create a 2D array for the map, not neccessary for data already in 2D
lons, lats = np.meshgrid(lon[::stride],lat[::stride])

print (lons)
print (lon[::stride])


# clevs = np.arange(0,100,5)
# x,y = map(lons,lats)
# cs = map.contour(x,y,u[0,0,:,:],clevs,colors='red',linewidths=1)
# p_lons = lons#[::10]
# p_lats = lats#[::10]
# p_u = u[0,0,::stride,::stride]
# p_v = v[0,0,::stride,::stride]

# cs = map.quiver(p_lons, p_lats, p_u, p_v, latlon=True)
# plt.show()
