import netCDF4 as nc
from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits
from mpl_toolkits.basemap import Basemap

nc = NetCDFFile('oscar_vel10004')

lat = nc.variables['float64 latitude'][:]
lon = nc.variables['float64 longitude'][:]
time = nc.variables['int32 time'][:]

