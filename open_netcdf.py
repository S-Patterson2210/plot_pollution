import netCDF4 as nc


fn = './oscar_vel10004.nc'
ds = nc.Dataset(fn)

print (ds)

print(ds.__dict__['YEAR'])






