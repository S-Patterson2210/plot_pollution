import netCDF4 as nc


fn = './AQUA_MODIS.20211024T025501.L2.SST.NRT.nc'
ds = nc.Dataset(fn)

# print (ds)
# print (ds.groups['geophysical_data'])
# lon = ds.groups['navigation_data']['longitude']
# lon = lon[:2020,:]
# lat = ds.groups['navigation_data']['latitude']
# lat = lat[:2020,:]
sst = ds.groups['geophysical_data']['sst'][:]
# sst = sst[:2020,:2020]
# print (lat)
# print (lon)
print (sst)
# lat = ds.variables['latitude'][:]
# lon = ds.variables['longitude'][:]
# time = ds.variables['time'][:]
# depth = ds.variables['depth'][:]
# u = ds.variables['u'][:]
# v = ds.variables['v'][:]


# print(u)
# print(lon)
# print(time)
# print(depth)


# vars = ds.variables
# for v in vars:
#     print (v)

