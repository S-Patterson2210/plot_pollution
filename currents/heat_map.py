import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits
from mpl_toolkits.basemap import Basemap
import math

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

map = Basemap(projection='merc',llcrnrlon=0.,llcrnrlat=-80.,urcrnrlon=360.,urcrnrlat=80.,resolution='h', suppress_ticks=False)

# Self explanatory but below is telling program to draw particulars of a map e.g coastlines
map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='linen', ocean_color='blue')



# Meshgrid tells the code to create a 2D array for the map, not neccessary for data already in 2D
stride = 1
lons, lats = np.meshgrid(lon[::stride],lat[::stride])
p_u = u[0,0,::stride,::stride]
p_v = v[0,0,::stride,::stride]

curr_mag = []
for u_row, v_row in zip(p_u, p_v):
    curr_row = []
    for u_val, v_val in zip (u_row, v_row):
        abs_val = math.sqrt(u_val*u_val+v_val*v_val) 
        curr_row.append(abs_val)
    curr_mag.append(curr_row)

x,y = map(lons,lats)
cs = map.pcolormesh(x,y,curr_mag)



# Meshgrid tells the code to create a 2D array for the map, not neccessary for data already in 2D
# stride = 3
# lons, lats = np.meshgrid(lon[::stride],lat[::stride])
# p_u = u[0,0,::stride,::stride]
# p_v = v[0,0,::stride,::stride]
# cs = map.quiver(lons, lats, p_u, p_v, latlon=True)

plt.show()
