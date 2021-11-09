import netCDF4 as nc

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits
from mpl_toolkits.basemap import Basemap, maskoceans
import math

# The below line denotes which file I am pulling the data from
ds = nc.Dataset('./AQUA_MODIS.20211024T025501.L2.SST.NRT.nc')


lat = ds.groups['navigation_data']['latitude'][:2020]
lon = ds.groups['navigation_data']['longitude'][:2020]
sst = ds.groups['geophysical_data']['sst'][:2020]

map = Basemap(projection='merc',llcrnrlon=0.,llcrnrlat=-80.,urcrnrlon=360.,urcrnrlat=80.,resolution='h')

# Self explanatory but below is telling program to draw particulars of a map e.g coastlines
map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='linen', ocean_color='blue')



# Meshgrid tells the code to create a 2D array for the map, not neccessary for data already in 2D
# stride = 1
# lons, lats = np.meshgrid(lon[::stride],lat[::stride])
# p_u = u[0,0,::stride,::stride]
# p_v = v[0,0,::stride,::stride]

# x,y = map(lon,lat)
cs = map.pcolormesh(lon,lat,sst,latlon = True)

# print (lat)
# print (lon)

# Meshgrid tells the code to create a 2D array for the map, not neccessary for data already in 2D
# stride = 3
# lons, lats = np.meshgrid(lon[::stride],lat[::stride])
# p_u = u[0,0,::stride,::stride]
# p_v = v[0,0,::stride,::stride]
# cs = map.quiver(lons, lats, p_u, p_v, latlon=True)

plt.show()
