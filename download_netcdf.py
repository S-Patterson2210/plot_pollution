import requests 
import matplotlib
import numpy

def download_netcdf(url, save_file):
    
    r = requests.get(url, allow_redirects=True)

    f = open (save_file, 'wb')
    f.write(r.content)

    f.close()

download_netcdf ('https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXADG.5.12.4/2021/08/MERRA2_400.tavg1_2d_adg_Nx.20210831.nc4', 'MERRA2_400.tavg1_2d_adg_Nx.20210831.nc4')

