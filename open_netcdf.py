import netCDF4 as nc


fn = './oscar_vel10004.nc'
ds = nc.Dataset(fn)

print (ds)

lat = ds.variables['latitude'][:]
lon = ds.variables['longitude'][:]
time = ds.variables['time'][:]
depth = ds.variables['depth'][:]

print(lat)
print(lon)
# print(time)
# print(depth)


# vars = ds.variables
# for v in vars:
#     print (v)

